---
# Documentation: https://wowchemy.com/docs/managing-content/

title: Cross-lingual Emotion Detection
subtitle: ''
summary: ''
authors:
- Sabit Hassan
- Shaden Shaar
- Kareem Darwish
tags: []
categories: []
date: '2022-06-01'
lastmod: 2023-03-27T23:52:25-04:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
publishDate: '2023-03-28T03:52:25.189754Z'
publication_types:
- '1'
abstract: 'Emotion detection can provide us with a window into understanding human
  behavior. Due to the complex dynamics of human emotions, however, constructing annotated
  datasets to train automated models can be expensive. Thus, we explore the efficacy
  of cross-lingual approaches that would use data from a source language to build
  models for emotion detection in a target language. We compare three approaches,
  namely: i) using inherently multilingual models; ii) translating training data into
  the target language; and iii) using an automatically tagged parallel corpus. In
  our study, we consider English as the source language with Arabic and Spanish as
  target languages. We study the effectiveness of different classification models
  such as BERT and SVMs trained with different features. Our BERT-based monolingual
  models that are trained on target language data surpass state-of-the-art (SOTA)
  by 4% and 5% absolute Jaccard score for Arabic and Spanish respectively. Next, we
  show that using cross-lingual approaches with English data alone, we can achieve
  more than 90% and 80% relative effectiveness of the Arabic and Spanish BERT models
  respectively. Lastly, we use LIME to analyze the challenges of training cross-lingual
  models for different language pairs.'
publication: '*Proceedings of the Thirteenth Language Resources and Evaluation Conference*'
links:
- name: URL
  url: https://aclanthology.org/2022.lrec-1.751
---
