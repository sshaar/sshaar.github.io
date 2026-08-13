export type PubType = 'journal' | 'conference' | 'workshop' | 'preprint';

export interface Publication {
  id: string;
  title: string;
  authors: string[];
  venue: string;
  venueShort?: string;
  year: number;
  type: PubType;
  projects: string[];
  url?: string;
  pdfUrl?: string;
  codeUrl?: string;
  bibtex?: string;
  citations?: number;
  findings?: boolean;
  /** Feature on the home page's "Selected papers" section. */
  selected?: boolean;
  /**
   * Figure/poster/diagram for the selected card.
   * Accepts any of:
   *   - a basename like `movierecapsqa` (resolves to `/public/publications/movierecapsqa.{png,jpg,webp,...}`)
   *   - a path relative to /public like `/publications/movierecapsqa.png`
   *   - an absolute URL
   * Supported extensions: .png .jpg .jpeg .webp .gif .svg .avif
   */
  image?: string;
  /** Short 1-3 sentence blurb shown on the selected card. */
  description?: string;
  /** Award or honor the paper received, shown as a badge on paper cards. */
  award?: string;
}

// Highlight author in rendered lists
export const ME = 'Shaden Shaar';

// Canonical author string reused across papers (keep short forms — display formatter will expand "et al." where needed)
export const publications: Publication[] = [
  {
    id: 'frye-2026-heart-transplant',
    title:
      'Thematic Analysis of Accepted Exception Requests for Heart Transplant Candidates Using a Large Language Model',
    authors: ['J. Frye', ME, 'C. Cardie', 'E. DeFilippis', 'D. Estrin', 'G. Sayer', 'N. Uriel', 'et al.'],
    venue: 'Journal of Heart and Lung Transplantation 45(5)',
    venueShort: 'JHLT',
    year: 2026,
    type: 'journal',
    projects: ['clinical'],
    url: 'https://www.jhltonline.org/article/S1053-2498(26)01051-X/fulltext',
    selected: true,
    image: '/publications/heart-transplant.jpg',
    description:
      'Uses an LLM to perform thematic analysis of accepted exception requests for heart transplant candidates, surfacing the clinical rationales that drive decisions in a setting where manual review at scale is infeasible.',
  },
  {
    id: 'shaar-2026-movierecapsqa',
    title: 'MovieRecapsQA: A Multimodal Open-Ended Video Question-Answering Benchmark',
    authors: [ME, 'B. Thymes', 'S. Chaixanien', 'C. Cardie', 'B. Hariharan'],
    venue: 'IEEE/CVF Conference on Computer Vision and Pattern Recognition',
    venueShort: 'CVPR',
    year: 2026,
    type: 'conference',
    projects: ['multimodal-video-qa'],
    url: 'https://arxiv.org/abs/2601.02536',
    selected: true,
    image: '/publications/movierecapsqa.jpg',
    description:
      'An open-ended video-QA benchmark built from movie recaps that stress-tests whether models can reason over long-form narrative, not just short clips. Paired with baselines that expose a large gap between human and model performance on grounded, cross-modal questions.',
  },
  {
    id: 'shaar-2025-triggers',
    title: 'Are Triggers Needed for Document-Level Event Extraction?',
    authors: [ME, 'W. Chen', 'M. Chatterjee', 'B. Wang', 'W. Zhao', 'C. Cardie'],
    venue: 'Transactions of the Association for Computational Linguistics 13',
    venueShort: 'TACL',
    year: 2025,
    type: 'journal',
    projects: ['event-extraction'],
    citations: 2,
    url: 'https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.51/134151',
    selected: true,
    image: '/publications/triggers.jpg',
    description:
      'Revisits a long-standing assumption in event extraction — that explicit trigger annotations are required — and shows that trigger-free formulations can match or exceed trigger-based pipelines at the document level.',
  },
  {
    id: 'chaixanien-2024-pungene',
    title: 'Pungene at DialAM-2024: Identification of Propositional and Illocutionary Relations',
    authors: ['S. Chaixanien', 'E. Choi', ME, 'C. Cardie'],
    venue: '11th Workshop on Argument Mining (ArgMining 2024)',
    venueShort: 'ArgMining',
    year: 2024,
    type: 'workshop',
    projects: ['argument-mining'],
    citations: 2,
  },
  {
    id: 'aydin-2024-edward-said',
    title: 'Edward Said at Touché: Human Value Detection Using Transformers and Upsampling',
    authors: ['A. N. Aydin', ME, 'C. Cardie'],
    venue: 'Conference and Labs of the Evaluation Forum (CLEF)',
    venueShort: 'CLEF',
    year: 2024,
    type: 'workshop',
    projects: ['values'],
    citations: 1,
  },
  {
    id: 'nakov-2022-checkthat-overview-clef',
    title:
      'Overview of the CLEF–2022 CheckThat! Lab on Fighting the COVID-19 Infodemic and Fake News Detection',
    authors: ['P. Nakov', 'A. Barrón-Cedeño', 'G. Da San Martino', 'F. Alam', 'J. M. Struss', 'T. Mandl', ME, 'et al.'],
    venue: 'International Conference of the Cross-Language Evaluation Forum',
    venueShort: 'CLEF',
    year: 2022,
    type: 'conference',
    projects: ['fact-checking', 'covid'],
    citations: 90,
  },
  {
    id: 'nakov-2022-checkthat-ecir',
    title:
      'The CLEF-2022 CheckThat! Lab on Fighting the COVID-19 Infodemic and Fake News Detection',
    authors: ['P. Nakov', 'A. Barrón-Cedeño', 'G. Da San Martino', 'F. Alam', 'J. M. Struss', 'T. Mandl', ME, 'et al.'],
    venue: 'European Conference on Information Retrieval',
    venueShort: 'ECIR',
    year: 2022,
    type: 'conference',
    projects: ['fact-checking', 'covid'],
    citations: 88,
  },
  {
    id: 'nakov-2022-checkthat-task2',
    title: 'Overview of the CLEF-2022 CheckThat! Lab Task 2 on Detecting Previously Fact-Checked Claims',
    authors: ['P. Nakov', 'G. Da San Martino', 'F. Alam', ME, 'H. Mubarak', 'N. Babulkov'],
    venue: 'CEUR Workshop Proceedings 3180',
    venueShort: 'CEUR',
    year: 2022,
    type: 'workshop',
    projects: ['fact-checking'],
    citations: 24,
  },
  {
    id: 'nakov-2022-checkthat-task1',
    title: 'Overview of the CLEF-2022 CheckThat! Lab Task 1 on Identifying Relevant Claims in Tweets',
    authors: ['P. Nakov', 'A. Barrón-Cedeño', 'G. Da San Martino', 'F. Alam', 'R. Míguez', ME, 'et al.'],
    venue: 'CEUR Workshop Proceedings 3180',
    venueShort: 'CEUR',
    year: 2022,
    type: 'workshop',
    projects: ['fact-checking'],
    citations: 83,
  },
  {
    id: 'shaar-2021-nlp4if',
    title: 'Findings of the NLP4IF-2021 Shared Tasks on Fighting the COVID-19 Infodemic and Censorship Detection',
    authors: [ME, 'F. Alam', 'G. Da San Martino', 'A. Nikolov', 'W. Zaghouani', 'P. Nakov', 'et al.'],
    venue: 'ACL NLP4IF Workshop 2021',
    venueShort: 'NLP4IF',
    year: 2021,
    type: 'workshop',
    projects: ['covid', 'fact-checking'],
    citations: 52,
  },
  {
    id: 'nakov-2022-second-pandemic',
    title: 'A Second Pandemic? Analysis of Fake News about COVID-19 Vaccines in Qatar',
    authors: ['P. Nakov', 'F. Alam', ME, 'G. Da San Martino', 'Y. Zhang'],
    venue: 'Findings of NAACL 2022',
    venueShort: 'NAACL',
    year: 2022,
    type: 'conference',
    projects: ['covid'],
    citations: 33,
    findings: true,
  },
  {
    id: 'shaar-2022-assisting-fact-checkers',
    title: 'Assisting the Human Fact-Checkers: Detecting All Previously Fact-Checked Claims in a Document',
    authors: [ME, 'N. Georgiev', 'F. Alam', 'G. Da San Martino', 'A. Mohamed', 'P. Nakov'],
    venue: 'Findings of EMNLP 2022',
    venueShort: 'EMNLP',
    year: 2022,
    type: 'conference',
    projects: ['fact-checking'],
    citations: 45,
    findings: true,
    url: 'https://aclanthology.org/2022.findings-emnlp.151/',
    selected: true,
    image: '/publications/assisting-fact-checkers.jpg',
    description:
      'Scales fact-checked-claim detection from isolated sentences to full documents, where each claim must be located and matched jointly. Introduces a document-level dataset and retrieval+ranking system tuned for real fact-checker workflows.',
  },
  {
    id: 'nakov-2021-checkthat-overview',
    title:
      'Overview of the CLEF–2021 CheckThat! Lab on Detecting Check-Worthy Claims, Previously Fact-Checked Claims, and Fake News',
    authors: ['P. Nakov', 'G. Da San Martino', 'T. Elsayed', 'A. Barrón-Cedeño', 'R. Míguez', ME, 'et al.'],
    venue: 'Cross-Language Evaluation Forum Conference',
    venueShort: 'CLEF',
    year: 2021,
    type: 'conference',
    projects: ['fact-checking'],
    citations: 119,
  },
  {
    id: 'nakov-2021-bulgarian-covid',
    title: 'COVID-19 in Bulgarian Social Media: Factuality, Harmfulness, Propaganda, and Framing',
    authors: ['P. Nakov', 'F. Alam', ME, 'G. Da San Martino', 'Y. Zhang'],
    venue: 'Recent Advances in Natural Language Processing',
    venueShort: 'RANLP',
    year: 2021,
    type: 'conference',
    projects: ['covid', 'propaganda'],
    citations: 29,
  },
  {
    id: 'dimitrov-2021-propaganda-memes',
    title: 'Detecting Propaganda Techniques in Memes',
    authors: ['D. Dimitrov', 'B. B. Ali', ME, 'F. Alam', 'F. Silvestri', 'H. Firooz', 'P. Nakov', 'et al.'],
    venue: 'ACL 2021',
    venueShort: 'ACL',
    year: 2021,
    type: 'conference',
    projects: ['propaganda'],
    citations: 135,
  },
  {
    id: 'skuczynska-2021-beasku',
    title: 'BeaSku at CheckThat! 2021: Fine-tuning Sentence BERT with Triplet Loss and Limited Data',
    authors: ['B. Skuczynska', ME, 'J. Spenader', 'P. Nakov'],
    venue: 'CLEF 2021 Conference and Labs of the Evaluation Forum',
    venueShort: 'CLEF',
    year: 2021,
    type: 'workshop',
    projects: ['fact-checking'],
    citations: 8,
  },
  {
    id: 'hassan-2022-crosslingual-emotion',
    title: 'Cross-Lingual Emotion Detection',
    authors: ['S. Hassan', ME, 'K. Darwish'],
    venue: 'LREC 2022',
    venueShort: 'LREC',
    year: 2022,
    type: 'conference',
    projects: ['emotion'],
    citations: 32,
  },
  {
    id: 'alam-2021-infodemic',
    title: 'Fighting the COVID-19 Infodemic in Social Media: A Holistic Perspective and a Call to Arms',
    authors: ['F. Alam', 'F. Dalvi', ME, 'N. Durrani', 'H. Mubarak', 'A. Nikolov', 'et al.'],
    venue: 'AAAI Conference on Web and Social Media 15',
    venueShort: 'ICWSM',
    year: 2021,
    type: 'conference',
    projects: ['covid', 'fact-checking'],
    citations: 163,
  },
  {
    id: 'dimitrov-2021-semeval-persuasion',
    title: 'SemEval-2021 Task 6: Detection of Persuasion Techniques in Texts and Images',
    authors: ['D. Dimitrov', 'B. B. Ali', ME, 'F. Alam', 'F. Silvestri', 'H. Firooz', 'P. Nakov', 'et al.'],
    venue: 'ACL-IJCNLP SemEval Workshop 2021',
    venueShort: 'SemEval',
    year: 2021,
    type: 'workshop',
    projects: ['propaganda'],
    citations: 173,
  },
  {
    id: 'shaar-2021-context',
    title: 'The Role of Context in Detecting Previously Fact-Checked Claims',
    authors: [ME, 'F. Alam', 'G. Da San Martino', 'P. Nakov'],
    venue: 'RANLP 2021',
    venueShort: 'RANLP',
    year: 2021,
    type: 'conference',
    projects: ['fact-checking'],
    citations: 52,
  },
  {
    id: 'nakov-2021-checkthat-ecir',
    title:
      'The CLEF-2021 CheckThat! Lab on Detecting Check-Worthy Claims, Previously Fact-Checked Claims, and Fake News',
    authors: ['P. Nakov', 'G. Da San Martino', 'T. Elsayed', 'A. Barrón-Cedeño', 'R. Míguez', ME, 'et al.'],
    venue: 'European Conference on Information Retrieval',
    venueShort: 'ECIR',
    year: 2021,
    type: 'conference',
    projects: ['fact-checking'],
    citations: 155,
  },
  {
    id: 'alam-2022-multimodal-disinfo',
    title: 'A Survey on Multimodal Disinformation Detection',
    authors: ['F. Alam', 'S. Cresci', 'T. Chakraborty', 'F. Silvestri', 'D. Dimitrov', 'G. Da San Martino', ME, 'et al.'],
    venue: 'COLING 2022',
    venueShort: 'COLING',
    year: 2022,
    type: 'conference',
    projects: ['fact-checking', 'propaganda'],
    citations: 224,
  },
  {
    id: 'nakov-2021-automated-fact-checking-ijcai',
    title: 'Automated Fact-Checking for Assisting Human Fact-Checkers',
    authors: ['P. Nakov', 'D. Corney', 'M. Hasanain', 'F. Alam', 'T. Elsayed', 'A. Barrón-Cedeño', ME, 'et al.'],
    venue: 'IJCAI 2021',
    venueShort: 'IJCAI',
    year: 2021,
    type: 'conference',
    projects: ['fact-checking'],
    citations: 386,
  },
  {
    id: 'shaar-2021-checkthat-task2',
    title:
      'Overview of the CLEF-2021 CheckThat! Lab Task 2 on Detecting Previously Fact-Checked Claims in Tweets and Political Debates',
    authors: [ME, 'F. Haouari', 'W. Mansour', 'M. Hasanain', 'N. Babulkov', 'F. Alam', 'et al.'],
    venue: 'CEUR-WS 2021',
    venueShort: 'CEUR',
    year: 2021,
    type: 'workshop',
    projects: ['fact-checking'],
    citations: 42,
  },
  {
    id: 'alam-2021-checkthat-task1',
    title: 'Overview of the CLEF-2021 CheckThat! Lab Task 1 on Check-Worthiness Estimation in Tweets and Political Debates',
    authors: ['F. Alam', ME, 'et al.'],
    venue: 'CEUR-WS 2021',
    venueShort: 'CEUR',
    year: 2021,
    type: 'workshop',
    projects: ['fact-checking'],
    citations: 82,
  },
  {
    id: 'barron-2020-checkthat-overview',
    title: 'Overview of CheckThat! 2020: Automatic Identification and Verification of Claims in Social Media',
    authors: ['A. Barrón-Cedeño', 'T. Elsayed', 'P. Nakov', 'G. Da San Martino', 'M. Hasanain', ME, 'et al.'],
    venue: 'Cross-Language Evaluation Forum',
    venueShort: 'CLEF',
    year: 2020,
    type: 'conference',
    projects: ['fact-checking'],
    citations: 186,
  },
  {
    id: 'dasanmartino-2020-prta',
    title: 'Prta: A System to Support the Analysis of Propaganda Techniques in the News',
    authors: ['G. Da San Martino', ME, 'Y. Zhang', 'S. Yu', 'A. Barrón-Cedeño', 'P. Nakov'],
    venue: 'ACL 2020',
    venueShort: 'ACL',
    year: 2020,
    type: 'conference',
    projects: ['propaganda'],
    citations: 93,
    url: 'https://arxiv.org/abs/2005.05854',
    selected: true,
    award: 'Best Demo Award, Honorable Mention',
    image: '/publications/prta.jpg',
    description:
      'An end-to-end system for highlighting 18 propaganda techniques in news articles, paired with a public web interface. Recognized with an Honorable Mention for Best Demo at ACL 2020.',
  },
  {
    id: 'shaar-2020-known-lie',
    title: 'That Is a Known Lie: Detecting Previously Fact-Checked Claims',
    authors: [ME, 'G. Da San Martino', 'N. Babulkov', 'P. Nakov'],
    venue: 'ACL 2020',
    venueShort: 'ACL',
    year: 2020,
    type: 'conference',
    projects: ['fact-checking'],
    citations: 241,
    url: 'https://aclanthology.org/2020.acl-main.332/',
    selected: true,
    image: '/publications/known-lie.jpg',
    description:
      'Formalizes "previously fact-checked claim detection" as a ranking task and releases the first dataset for it, showing that reusing existing fact-checks is a practical alternative to verifying every claim from scratch.',
  },
  {
    id: 'alam-2021-infodemic-emnlp',
    title:
      'Fighting the COVID-19 Infodemic: Modeling the Perspective of Journalists, Fact-Checkers, Social Media Platforms, Policy Makers, and the Society',
    authors: ['F. Alam', ME, 'F. Dalvi', 'H. Sajjad', 'A. Nikolov', 'H. Mubarak', 'G. Da San Martino', 'et al.'],
    venue: 'Findings of EMNLP 2021',
    venueShort: 'EMNLP',
    year: 2020,
    type: 'conference',
    projects: ['covid', 'fact-checking'],
    citations: 233,
    findings: true,
  },
  {
    id: 'shaar-2020-checkthat-english',
    title: 'Overview of CheckThat! 2020 English: Automatic Identification and Verification of Claims in Social Media',
    authors: [ME, 'A. Nikolov', 'N. Babulkov', 'F. Alam', 'A. Barrón-Cedeño', 'T. Elsayed', 'et al.'],
    venue: 'CLEF Working Notes',
    venueShort: 'CLEF',
    year: 2020,
    type: 'workshop',
    projects: ['fact-checking'],
    citations: 79,
  },
  {
    id: 'hassan-2018-interactive-classifiers',
    title: 'Interactive Evaluation of Classifiers under Limited Resources',
    authors: ['S. Hassan', ME, 'B. Raj', 'S. Razak'],
    venue: '17th IEEE International Conference on Machine Learning and Applications',
    venueShort: 'ICMLA',
    year: 2018,
    type: 'conference',
    projects: ['early'],
    citations: 6,
  },
  {
    id: 'shaar-2018-group-identification',
    title: 'Group Identification in Crowded Environments Using Proximity Sensing',
    authors: [ME, 'S. Razak', 'F. Dalvi', 'S. A. H. Moosavi'],
    venue: 'IEEE 43rd Conference on Local Computer Networks',
    venueShort: 'LCN',
    year: 2018,
    type: 'conference',
    projects: ['early'],
  },
];

export const publicationsByYear = () => {
  const byYear = new Map<number, Publication[]>();
  for (const pub of publications) {
    const list = byYear.get(pub.year) ?? [];
    list.push(pub);
    byYear.set(pub.year, list);
  }
  return [...byYear.entries()].sort((a, b) => b[0] - a[0]);
};
