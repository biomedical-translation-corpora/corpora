
import os
import sys

from langdetect import detect

from Bio import Entrez
Entrez.email = "EMAIL"

# pubmed

def get_set_articles(records):
	return records["PubmedArticle"]

def get_pmid(record):
	return record["MedlineCitation"]["PMID"]

def get_abstract_text(record):
	all_abstracttexts = []
	try:
		texts = []
		texts.append(record["MedlineCitation"]["Article"]['Abstract']['AbstractText'])
		if 'OtherAbstract' in record["MedlineCitation"]:
			for item in record["MedlineCitation"]['OtherAbstract']:
				texts.append(item['AbstractText'])
		abstracttext = ""
		for text in texts:
			if len(text)>1:
				abstracttext = ""
				for part in text:
					if len(part.attributes)>0:
						label = part.attributes['Label']
					else:
						label = 'None'
					part = part.replace('"', "'")
					abstracttext += part+" "
			else:
				abstracttext = text[0]
				abstracttext = abstracttext.replace('"',"'")
			all_abstracttexts.append(abstracttext.strip())
	except:
		print('PMID '+get_pmid(record)+' - abstract not found!')
	return all_abstracttexts

def build_article(record):
	articles = []	
	langs = []
	all_abstracttexts = get_abstract_text(record)
	for index in range(0,len(all_abstracttexts)):
		article = {}
		article["pmid"] = get_pmid(record)
		article["abstracttext"] = all_abstracttexts[index]
		# lang
		lang = detect(article["abstracttext"]) 
		article["lang"] = lang
		langs.append(lang)
		articles.append(article)
	return articles, langs

# fetch

def fetch_pubmed_articles(ids):
	ids = ",".join(ids)
	handle = Entrez.efetch(db="pubmed", id=ids, retmode="xml")
	records = Entrez.read(handle)
	#print(records)
	set_articles = []
	set_langs = []
	for record in get_set_articles(records):
		#print(record)
		article, langs = build_article(record)
		set_articles.append(article)
		set_langs.append(langs)
	handle.close()
	#print(len(articles))
	return set_articles, set_langs

def fetch_multiple_articles(pmids, out_dir, lang1, lang2):
	print(pmids)
	set_articles, set_langs = fetch_pubmed_articles(pmids)
	for index in range(0,len(set_articles)):
		langs = set_langs[index]
		#print(langs)
		if len(langs)<2 or lang1 not in langs or lang2 not in langs:
			continue
		article = set_articles[index]
		for item in article:
			lang = detect(item["abstracttext"])
			if lang!=lang1 and lang!=lang2:
				continue
			print(item["pmid"])
			print(item["abstracttext"])
			print(item["lang"])
			with open(os.path.join(out_dir,item["pmid"]+"_"+item["lang"]+".txt"), "w") as writer:
				writer.write(item["abstracttext"]+"\n")
			writer.close()

map_langs = {
	"eng": "en",
	"ita": "it",
	"chi": "zh-cn",
	"fre": "fr",
	"ger": "de",
	"por": "pt",
	"spa": "es",
	"rus": "ru" 
}

def get_lang1_lang2(filename):
	lang1, lang2 = filename[0:7].split("_")
	lang1 = map_langs[lang1]
	lang2 = map_langs[lang2]
	return lang1, lang2

def retrieve_abstracts(filename, out_dir):
	lang1, lang2 = get_lang1_lang2(filename)
	pmids = []	
	with open(os.path.join(filename), "r") as reader:
		lines = reader.readlines()
		for line in lines:
			pmid = line.strip()
			pmids.append(pmid)
			if len(pmids)<100:
				continue
			# fetch
			fetch_multiple_articles(pmids,out_dir,lang1,lang2)
			pmids = []
	if len(pmids)>0:
		fetch_multiple_articles(pmids, out_dir, lang1, lang2)

if __name__ == '__main__':
	retrieve_abstracts(sys.argv[1],sys.argv[2])


