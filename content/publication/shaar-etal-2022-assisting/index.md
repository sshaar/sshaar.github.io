---
# Documentation: https://wowchemy.com/docs/managing-content/

title: 'Assisting the Human Fact-Checkers: Detecting All Previously Fact-Checked Claims
  in a Document'
subtitle: ''
summary: ''
authors:
- Shaden Shaar
- Nikola Georgiev
- Firoj Alam
- Giovanni Da San Martino
- Aisha Mohamed
- Preslav Nakov
tags: []
categories: []
date: '2022-12-01'
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
publishDate: '2023-03-28T03:52:25.520349Z'
publication_types:
- '1'
abstract: Given the recent proliferation of false claims online, there has been a
  lot of manual fact-checking effort. As this is very time-consuming, human fact-checkers
  can benefit from tools that can support them and make them more efficient. Here,
  we focus on building a system that could provide such support. Given an input document,
  it aims to detect all sentences that contain a claim that can be verified by some
  previously fact-checked claims (from a given database). The output is a re-ranked
  list of the document sentences, so that those that can be verified are ranked as
  high as possible, together with corresponding evidence. Unlike previous work, which
  has looked into claim retrieval, here we take a document-level perspective. We create
  a new manually annotated dataset for the task, and we propose suitable evaluation
  measures. We further experiment with a learning-to-rank approach, achieving sizable
  performance gains over several strong baselines. Our analysis demonstrates the importance
  of modeling text similarity and stance, while also taking into account the veracity
  of the retrieved previously fact-checked claims. We believe that this research would
  be of interest to fact-checkers, journalists, media, and regulatory authorities.
publication: '*Findings of the Association for Computational Linguistics: EMNLP 2022*'
links:
- name: URL
  url: https://aclanthology.org/2022.findings-emnlp.151
---
