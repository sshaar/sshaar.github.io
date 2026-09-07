export type ProjectColor =
  | 'amber'
  | 'sky'
  | 'emerald'
  | 'rose'
  | 'teal'
  | 'violet'
  | 'pink'
  | 'orange'
  | 'fuchsia'
  | 'slate';

export interface ResearchProject {
  slug: string;
  name: string;
  short?: string;
  summary: string;
  color: ProjectColor;
}

export const projects: ResearchProject[] = [
  {
    slug: 'multimodal-video-qa',
    name: 'Long-Form Video Understanding',
    short: 'Long-form Video',
    color: 'sky',
    summary:
      'Open-ended question-answering over full-length narrative video — what a model has to locate in a two-hour film, and when locating the right scene is not enough.',
  },
  {
    slug: 'fact-checking',
    name: 'Fact-checking & Claim Detection',
    short: 'Fact-checking',
    color: 'emerald',
    summary:
      'Building systems that assist human fact-checkers: identifying check-worthy claims, matching them to previously fact-checked evidence, and the shared-task ecosystem around them (CLEF CheckThat!).',
  },
  {
    slug: 'propaganda',
    name: 'Propaganda & Persuasion Detection',
    short: 'Propaganda',
    color: 'rose',
    summary:
      'Detecting propaganda and persuasion techniques across text, images, and memes, including the Prta analysis system and SemEval-2021 Task 6.',
  },
  {
    slug: 'covid',
    name: 'COVID-19 Misinformation',
    short: 'COVID-19',
    color: 'teal',
    summary:
      'Analyzing and combating pandemic-era misinformation across languages and platforms — factuality, harmfulness, framing, and vaccine discourse.',
  },
  {
    slug: 'argument-mining',
    name: 'Argument Mining',
    short: 'Argument',
    color: 'violet',
    summary:
      'Identifying propositional and illocutionary relations in argumentative dialogue (DialAM 2024).',
  },
  {
    slug: 'event-extraction',
    name: 'Event Extraction',
    short: 'Events',
    color: 'amber',
    summary:
      'Document-level event extraction — revisiting whether trigger annotations are necessary and building trigger-free models that match or exceed trigger-based pipelines.',
  },
  {
    slug: 'clinical',
    name: 'Clinical NLP',
    short: 'Clinical',
    color: 'pink',
    summary:
      'Using LLMs to surface clinical decision patterns from unstructured medical narratives, with a focus on heart failure and heart transplant care — in collaboration with NewYork-Presbyterian Hospital.',
  },
  {
    slug: 'values',
    name: 'Human Values Detection',
    short: 'Values',
    color: 'orange',
    summary:
      'Identifying human values expressed in argumentative text (Touché 2024).',
  },
  {
    slug: 'emotion',
    name: 'Emotion Detection',
    short: 'Emotion',
    color: 'fuchsia',
    summary: 'Cross-lingual emotion classification across varied language resources.',
  },
  {
    slug: 'early',
    name: 'Early Work',
    short: 'Early',
    color: 'slate',
    summary: 'Undergraduate research on interactive classification and proximity-sensing group identification.',
  },
];

export const getProject = (slug: string) => projects.find((p) => p.slug === slug);

/**
 * Full class strings per color — written out so Tailwind's JIT picks them up.
 * `chip` is the filter button (off state); `chipActive` is its on state; `tag`
 * is the small inline tag shown on each publication card.
 */
export const COLOR_CLASSES: Record<
  ProjectColor,
  { chip: string; chipActive: string; tag: string }
> = {
  amber: {
    chip: 'border-[#ddc9a3] text-[#6f5324] hover:border-[#c9ae7e] hover:bg-[#f2ead9] dark:border-amber-900/60 dark:text-amber-300 dark:hover:bg-amber-900/20',
    chipActive: 'border-[#c9ae7e] bg-[#f2ead9] text-[#6f5324] dark:border-amber-400 dark:bg-amber-900/40 dark:text-amber-100',
    tag: 'bg-[#f2ead9] text-[#6f5324] hover:bg-[#e8dcc5] dark:bg-amber-900/40 dark:text-amber-200 dark:hover:bg-amber-900/60',
  },
  sky: {
    chip: 'border-[#b9cfdd] text-[#2b5871] hover:border-[#8fb4ca] hover:bg-[#e3ecf2] dark:border-sky-900/60 dark:text-sky-300 dark:hover:bg-sky-900/20',
    chipActive: 'border-[#8fb4ca] bg-[#e3ecf2] text-[#2b5871] dark:border-sky-400 dark:bg-sky-900/40 dark:text-sky-100',
    tag: 'bg-[#e3ecf2] text-[#2b5871] hover:bg-[#d3e2eb] dark:bg-sky-900/40 dark:text-sky-200 dark:hover:bg-sky-900/60',
  },
  emerald: {
    chip: 'border-[#b6cfc0] text-[#2f5c46] hover:border-[#8db4a0] hover:bg-[#dfeae2] dark:border-emerald-900/60 dark:text-emerald-300 dark:hover:bg-emerald-900/20',
    chipActive: 'border-[#8db4a0] bg-[#dfeae2] text-[#2f5c46] dark:border-emerald-400 dark:bg-emerald-900/40 dark:text-emerald-100',
    tag: 'bg-[#dfeae2] text-[#2f5c46] hover:bg-[#cfded4] dark:bg-emerald-900/40 dark:text-emerald-200 dark:hover:bg-emerald-900/60',
  },
  rose: {
    chip: 'border-[#dcbdbf] text-[#7a3b42] hover:border-[#c79a9d] hover:bg-[#f2e4e3] dark:border-rose-900/60 dark:text-rose-300 dark:hover:bg-rose-900/20',
    chipActive: 'border-[#c79a9d] bg-[#f2e4e3] text-[#7a3b42] dark:border-rose-400 dark:bg-rose-900/40 dark:text-rose-100',
    tag: 'bg-[#f2e4e3] text-[#7a3b42] hover:bg-[#e8d3d2] dark:bg-rose-900/40 dark:text-rose-200 dark:hover:bg-rose-900/60',
  },
  teal: {
    chip: 'border-[#b3d0ca] text-[#285d57] hover:border-[#8ab5ad] hover:bg-[#deebe8] dark:border-teal-900/60 dark:text-teal-300 dark:hover:bg-teal-900/20',
    chipActive: 'border-[#8ab5ad] bg-[#deebe8] text-[#285d57] dark:border-teal-400 dark:bg-teal-900/40 dark:text-teal-100',
    tag: 'bg-[#deebe8] text-[#285d57] hover:bg-[#cee0dc] dark:bg-teal-900/40 dark:text-teal-200 dark:hover:bg-teal-900/60',
  },
  violet: {
    chip: 'border-[#c4bddd] text-[#4b4477] hover:border-[#a49ac6] hover:bg-[#e7e5f1] dark:border-violet-900/60 dark:text-violet-300 dark:hover:bg-violet-900/20',
    chipActive: 'border-[#a49ac6] bg-[#e7e5f1] text-[#4b4477] dark:border-violet-400 dark:bg-violet-900/40 dark:text-violet-100',
    tag: 'bg-[#e7e5f1] text-[#4b4477] hover:bg-[#d9d6e9] dark:bg-violet-900/40 dark:text-violet-200 dark:hover:bg-violet-900/60',
  },
  pink: {
    chip: 'border-[#ddbecb] text-[#77394f] hover:border-[#c99cb0] hover:bg-[#f2e4ea] dark:border-pink-900/60 dark:text-pink-300 dark:hover:bg-pink-900/20',
    chipActive: 'border-[#c99cb0] bg-[#f2e4ea] text-[#77394f] dark:border-pink-400 dark:bg-pink-900/40 dark:text-pink-100',
    tag: 'bg-[#f2e4ea] text-[#77394f] hover:bg-[#e7d3dc] dark:bg-pink-900/40 dark:text-pink-200 dark:hover:bg-pink-900/60',
  },
  orange: {
    chip: 'border-[#dfc3a8] text-[#7a4a29] hover:border-[#cba482] hover:bg-[#f3e7dc] dark:border-orange-900/60 dark:text-orange-300 dark:hover:bg-orange-900/20',
    chipActive: 'border-[#cba482] bg-[#f3e7dc] text-[#7a4a29] dark:border-orange-400 dark:bg-orange-900/40 dark:text-orange-100',
    tag: 'bg-[#f3e7dc] text-[#7a4a29] hover:bg-[#e9d8c8] dark:bg-orange-900/40 dark:text-orange-200 dark:hover:bg-orange-900/60',
  },
  fuchsia: {
    chip: 'border-[#d7bcd4] text-[#6d3768] hover:border-[#bf9bbb] hover:bg-[#eee3ed] dark:border-fuchsia-900/60 dark:text-fuchsia-300 dark:hover:bg-fuchsia-900/20',
    chipActive: 'border-[#bf9bbb] bg-[#eee3ed] text-[#6d3768] dark:border-fuchsia-400 dark:bg-fuchsia-900/40 dark:text-fuchsia-100',
    tag: 'bg-[#eee3ed] text-[#6d3768] hover:bg-[#e2d2e1] dark:bg-fuchsia-900/40 dark:text-fuchsia-200 dark:hover:bg-fuchsia-900/60',
  },
  slate: {
    chip: 'border-[#cbc6bc] text-[#4c4941] hover:border-[#aea89b] hover:bg-[#e8e5df] dark:border-slate-900/60 dark:text-slate-300 dark:hover:bg-slate-900/20',
    chipActive: 'border-[#aea89b] bg-[#e8e5df] text-[#4c4941] dark:border-slate-400 dark:bg-slate-900/40 dark:text-slate-100',
    tag: 'bg-[#e8e5df] text-[#4c4941] hover:bg-[#dcd8d0] dark:bg-slate-900/40 dark:text-slate-200 dark:hover:bg-slate-900/60',
  },
};
