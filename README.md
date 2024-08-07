## Welcome to the repositories of the WMT Biomedical Translation Task

Here we host various datasets that we have compiled for the [Biomedical Translation Task](http://www.statmt.org/wmt21/biomedical-translation-task.html) at [WMT](http://www.statmt.org/wmt21/index.html).

- Medline dataset of titles and abstracts of scientific publications (FR/EN, PT/EN, ES/EN, DE/EN, ZH/EN, RO/EN, IT/EN, RU/EN)
- Scielo of scientific publications (FR/EN, PT/EN, ES/PT)
- EDP dataset of scientific publications (FR/EN)
- ReBEC clinical trials (PT/EN)

### List of corpora

#### Medline corpus

| datasets   |  2016 |  2017 |  2018 |  2019 |  2020 |  2021 |  2022 |  2023 |  2024 |
| ---------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| training   | [WMT'16](https://zenodo.org/record/5552299#.YV1orSWxUog) | | | [WMT'19](https://drive.google.com/drive/folders/1yBfh_KFSN0XxP2k9rnkxKNKYvjpj703p) | [WMT'20](https://drive.google.com/drive/folders/1G_OTHKDJ4vmZB-5TFDZPc7tYigw-JYBI?usp=sharing) | | [WMT'22](trainWmt22.zip)<sup>1</sup> | | | 
| test set   | | | [WMT'18](https://drive.google.com/drive/u/1/folders/1hmn24Xr1gJIQ9tsYwUJGgia19davCNz9) | [WMT'19](https://drive.google.com/drive/u/0/folders/1x4689LkvdJTyAxsB6tYu12MJzxgiyDZ_) | [WMT'20](https://drive.google.com/drive/u/1/folders/1G_OTHKDJ4vmZB-5TFDZPc7tYigw-JYBI) | [WMT'21](https://drive.google.com/drive/u/1/folders/1ujEhu_fAW6Ufo9KGYBqW8TYLc8kYSspz) | [WMT'22](https://drive.google.com/drive/folders/1W_zVbS5yb921bpSZW-Ca9nKoWXmim1xU?usp=sharing) | [WMT'23](https://drive.google.com/drive/folders/1BLS8o5wpXz4QQhM8XDVvtJEz4veHMB8s?usp=sharing) | [WMT'24](https://drive.google.com/drive/folders/18lQAS1ixUYmmeR8-WnCK3ZODjLRi6Oni?usp=sharing) |

<sup>1</sup> The parallel abstracts can be retrieved from Medline using our script: [wmtbio22_train_data.py](wmtbio22_train_data.py). It uses [biopython](https://biopython.org/docs/1.75/api/Bio.Entrez.html) and you'll need a valid email to access the data in Medline.

| training    |  2016  |  2019  |  2020  |  2022  |
| ----------  | ------ | ------ | ------ | ------ |
| en/es       |    x   |    x   |        |    x   |
| en/fr       |    x   |    x   |        |    x   |
| en/pt       |    x   |    x   |        |    x   |
| en/de       |        |    x   |        |    x   |
| en/it       |        |        |    x   |    x   |
| en/ru       |        |        |    x   |    x   |

| test set    |  2018  |  2019  |  2020  |  2021  | 
| ----------  | ------ | ------ | ------ | ------ | 
| en/es       |    x   |    x   |    x   |    x   |
| en/fr       |    x   |    x   |    x   |    x   |
| en/pt       |    x   |    x   |    x   |    x   |
| en/de       |    x   |    x   |    x   |    x   |
| en/zh       |    x   |    x   |    x   |    x   |
| en/ro       |    x   |        |        |        |
| en/it       |        |        |    x   |    x   |
| en/ru       |        |        |    x   |    x   |

#### Scielo corpus

| test set    | 2016  |  2017  | 
| ---------- | ------ | ------ | 
| en/es, en/fr, en/pt | [test WMT'16](https://zenodo.org/record/5589209) |  [test WMT'17](https://zenodo.org/record/843862) |

| training    | parallel  | monolingual  | 
| ---------- | ------ | ------ | 
| en/es, en/fr, en/pt | [training](https://zenodo.org/record/5588265) | [monolingual](https://zenodo.org/record/5588794) |

#### EDP corpus

| test set    | 2017  | 
| ---------- | ------ | 
| en/fr        | [test WMT'17](https://cabernet.limsi.fr/EDP_EN.html) |

#### ReBEC corpus

| training    |   | 
| ---------- | ------ | 
| en/pt      | [dataset](https://github.com/biomedical-translation-corpora/rebec)  |

### Publications

**Please cite our publications if you use our corpora.**

(WMT'22 Biomedical Task)
Neves M, Jimeno Yepes A, SiuA, Roller R, Thomas P, Vicente Navarro M, Yeganova L, Wiemann D, Di Nunzio GM, Vezzani F, Gerardin C, Bawden R, Johan Estrada D, Lima-Lopez S, Farre-Maduel E, Krallinger M, Grozea C, Neveol A. Findings of the WMT 2022 Biomedical Translation Shared Task: Monolingual Clinical Case Reports.
[PDF](https://www.statmt.org/wmt22/pdf/2022.wmt-1.69.pdf) [BibText](https://www.statmt.org/wmt22/bib/2022.wmt-1.69.bib)

(WMT'21 Biomedical Task)
Yeganova L, Wiemann D, Neves M, Vezzani F, Siu A, Jauregi Unanue I, Oronoz M, Mah N, Névéol A, Martinez D, Bawden R, Di Nunzio GM, Roller R, Thomas P, Grozea C, Perez-de-Viñaspre O, Vicente Navarro M and Jimeno Yepes A. Findings of the WMT 2021 Biomedical Translation Shared Task: Summaries of Animal Experiments as New Test Set, 6th Conference on Machine Translation, EMNLP 2021. [PDF and BibText](https://aclanthology.org/2021.wmt-1.70/)

(WMT'20 Biomedical Task)
Bawden R, Di Nunzio GM, Grozea C, Jauregi Unanue I, Jimeno Yepes A, Mah N, Martinez D, Neveol A, Neves M, Oronoz M, Perez de Viñaspre O, Piccardi M, Roller R, Siu A, Thomas P, Vezzani F, Vicente Navarro M, Wiemann D, Yeganova L. Findings of the WMT 2020 Biomedical Translation Shared Task: Basque, Italian and Russian as New Additional Languages, 5th Conference on Machine Translation, EMNLP 2020, online. [PDF and BibText](https://aclanthology.org/2020.wmt-1.76/)

(Survey of Authors’ Abstract Writing Practice)
Neveol A, Jimeno Yepes A, Neves M. MEDLINE as a Parallel Corpus: a Survey to Gain Insight on French-, Spanish-and Portuguese-Speaking Authors’ Abstract Writing Practice, 12th Language Resources and Evaluation Conference, LREC 2020, Marseille, France. [PDF and BibText](https://aclanthology.org/2020.lrec-1.453/)

(WMT'19 Biomedical Task)
Bawden R, Bretonnel Cohen K, Grozea C, Jimeno Yepes A, Kittner M, Krallinger M, Mah N, Neveol A, Neves M, Soares F, Siu A, Verspoor A, Vicente Navarro M. Findings of the WMT 2019 Biomedical Translation Shared Task: Evaluation for MEDLINE Abstracts and Biomedical Terminologies , 4th Conference on Machine Translation, ACL 2019, Florence, Italy.  [PDF and BibText](https://www.aclweb.org/anthology/W19-5403/)

(WMT'18 Biomedical Task)
Neves M, Jimeno Yepes A, Névéol A, Grozea C, Siu A, Kittner M, Verspoor K. Findings of the WMT 2018 Biomedical Translation Shared Task: Evaluation on Medline test sets, Proceedings of the Third Conference on Machine Trasnlation (WMT) at EMNLP, 2018, Brussels, Belgium. [PDF and BibText](https://www.aclweb.org/anthology/W18-6403/)

(Parallel Biomedical Corpora)
Névéol A, Jimeno Yepes A, Neves M, Verspoor K. Parallel Corpora for the Biomedical Domain, International Conference on Language Resources and Evaluation (LREC), 2018, Myazaki, Japan. [PDF and BibText](https://www.aclweb.org/anthology/L18-1043/)

(WMT'17 Biomedical Task)
Jimeno Yepes A, N&eacute;v&eacute;ol A, Neves M, Verspoor K, Bojar O, Boyer A, Grozea C, Haddow H, Kittner M, Lichtblau Y, Pecina P, Roller R, Rosa R, Siu A, Thomas P, Trescher S. Findings of the WMT 2017 Biomedical Translation Shared Task, Proceedings of the Second Conference on Machine Translation (WMT17) at the Conference on Empirical Methods on Natural Language Processing (EMNLP 2017), Copenhagen, Denmark. [PDF and BibText](https://www.aclweb.org/anthology/W17-4719/)

(WMT'16 Biomedical Task)
Bojar O, Chatterjee R, Federmann C, Graham Y, Haddow B, Huck M, Jimeno Yepes A, Koehn P, Logacheva V, Monz C, Negri M, N&eacute;v&eacute;ol A, Neves M, Popel M, Post M, Rubino R, Scarton C, Specia L, Turchi M, Verspoor K and Zampieri M. Findings of the 2016 Conference on Machine Translation, ACL 2016, Proceedings of the First Conference on Machine Translation (WMT16), pp. 131-198, 2016, Berlin, Germany. [PDF and BibText](https://www.aclweb.org/anthology/W16-2301/)

(Scielo corpus)
Neves M, Jimeno-Yepes A and N&eacute;v&eacute;ol A. The Scielo Corpus: a Parallel Corpus of Scientific Publications for Biomedicine, International Conference on Language Resources and Evaluation (LREC), 2016, Portoroz, Slovenia. [PDF and Bibtex](https://www.aclweb.org/anthology/L16-1470/)

### Support or Contact

Please contact us by [mail](wmtbiomedical@gmail.com). Please also join our [discussion forum](https://groups.google.com/forum/?hl=en#!forum/wmt-biomedical-task). 

- Antonio Jimeno Yepes (RMIT University, Australia)
- Aur&eacute;lie N&eacute;v&eacute;ol (LIMSI, CNRS, France)
- Mariana Neves (German Federal Institute for Risk Assessment, Germany)
