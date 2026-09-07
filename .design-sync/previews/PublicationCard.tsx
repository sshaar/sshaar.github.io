import * as React from 'react';
import { PublicationCard } from 'shaden-shaar-site';

const ME = 'Shaden Shaar';

/** The canonical case: a recent paper with a summary and thread tags. */
export const SelectedPaper = () => (
  <PublicationCard
    title="MovieRecapsQA: A Multimodal Open-Ended Video Question-Answering Benchmark"
    authors={['Shaden Shaar', 'Jordan Thymes', 'Pat Chaixanien', 'Claire Cardie', 'Bharath Hariharan']}
    me={ME}
    venue="CVPR"
    year={2026}
    url="https://arxiv.org/abs/2601.02536"
    description="8,231 open-ended questions over 60 full-length films, paired with atomic facts that support a reference-free factuality judge. Benchmarking seven MLLMs against human answerers shows perception, not reasoning, is the bottleneck."
    tags={[{ label: 'Long-form Generation', color: 'sky', href: '/publications/' }]}
  />
);

/** With an award badge above the title. */
export const WithAward = () => (
  <PublicationCard
    title="Prta: A System to Support the Analysis of Propaganda Techniques in the News"
    authors={['Giovanni Da San Martino', 'Shaden Shaar', 'Yifan Zhang', 'Seunghak Yu', 'Alberto Barrón-Cedeño', 'Preslav Nakov']}
    me={ME}
    venue="ACL"
    year={2020}
    url="https://arxiv.org/abs/2005.05854"
    award="Best Demo Award, Honorable Mention"
    description="An end-to-end system for highlighting 18 propaganda techniques in news articles, paired with a public web interface."
    tags={[{ label: 'Propaganda', color: 'rose', href: '/publications/' }]}
  />
);

/** A Findings-track paper carrying two thread tags. */
export const FindingsTrack = () => (
  <PublicationCard
    title="That Is a Known Lie: Detecting Previously Fact-Checked Claims"
    authors={['Shaden Shaar', 'Nikolay Babulkov', 'Giovanni Da San Martino', 'Preslav Nakov']}
    me={ME}
    venue="ACL"
    year={2020}
    findings
    url="https://arxiv.org/abs/2005.06058"
    description="Introduced the task of detecting claims that have already been fact-checked, now a standard step in automated fact-checking pipelines."
    tags={[
      { label: 'Fact-checking', color: 'emerald', href: '/publications/' },
      { label: 'COVID-19', color: 'teal', href: '/publications/' },
    ]}
  />
);

/** Minimal props — no summary, no tags, title not linked. */
export const Minimal = () => (
  <PublicationCard
    title="Are Triggers Needed for Document-Level Event Extraction?"
    authors={['Shaden Shaar', 'Wayne Chen', 'Maitreyi Chatterjee', 'Barry Wang', 'Wenting Zhao', 'Claire Cardie']}
    me={ME}
    venue="TACL"
    year={2025}
  />
);
