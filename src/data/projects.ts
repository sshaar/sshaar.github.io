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
    name: 'Multi-modal Long-form Generation',
    short: 'Long-form Generation',
    color: 'sky',
    summary:
      'Long-form question-answering and summarization over videos and other multi-modal narratives, with an emphasis on coherence across extended outputs.',
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
    chip: 'border-amber-200 text-amber-800 hover:border-amber-500 hover:bg-amber-50 dark:border-amber-900/60 dark:text-amber-300 dark:hover:bg-amber-900/20',
    chipActive: 'border-amber-500 bg-amber-100 text-amber-900 dark:border-amber-400 dark:bg-amber-900/40 dark:text-amber-100',
    tag: 'bg-amber-100 text-amber-800 hover:bg-amber-200 dark:bg-amber-900/40 dark:text-amber-200 dark:hover:bg-amber-900/60',
  },
  sky: {
    chip: 'border-sky-200 text-sky-800 hover:border-sky-500 hover:bg-sky-50 dark:border-sky-900/60 dark:text-sky-300 dark:hover:bg-sky-900/20',
    chipActive: 'border-sky-500 bg-sky-100 text-sky-900 dark:border-sky-400 dark:bg-sky-900/40 dark:text-sky-100',
    tag: 'bg-sky-100 text-sky-800 hover:bg-sky-200 dark:bg-sky-900/40 dark:text-sky-200 dark:hover:bg-sky-900/60',
  },
  emerald: {
    chip: 'border-emerald-200 text-emerald-800 hover:border-emerald-500 hover:bg-emerald-50 dark:border-emerald-900/60 dark:text-emerald-300 dark:hover:bg-emerald-900/20',
    chipActive: 'border-emerald-500 bg-emerald-100 text-emerald-900 dark:border-emerald-400 dark:bg-emerald-900/40 dark:text-emerald-100',
    tag: 'bg-emerald-100 text-emerald-800 hover:bg-emerald-200 dark:bg-emerald-900/40 dark:text-emerald-200 dark:hover:bg-emerald-900/60',
  },
  rose: {
    chip: 'border-rose-200 text-rose-800 hover:border-rose-500 hover:bg-rose-50 dark:border-rose-900/60 dark:text-rose-300 dark:hover:bg-rose-900/20',
    chipActive: 'border-rose-500 bg-rose-100 text-rose-900 dark:border-rose-400 dark:bg-rose-900/40 dark:text-rose-100',
    tag: 'bg-rose-100 text-rose-800 hover:bg-rose-200 dark:bg-rose-900/40 dark:text-rose-200 dark:hover:bg-rose-900/60',
  },
  teal: {
    chip: 'border-teal-200 text-teal-800 hover:border-teal-500 hover:bg-teal-50 dark:border-teal-900/60 dark:text-teal-300 dark:hover:bg-teal-900/20',
    chipActive: 'border-teal-500 bg-teal-100 text-teal-900 dark:border-teal-400 dark:bg-teal-900/40 dark:text-teal-100',
    tag: 'bg-teal-100 text-teal-800 hover:bg-teal-200 dark:bg-teal-900/40 dark:text-teal-200 dark:hover:bg-teal-900/60',
  },
  violet: {
    chip: 'border-violet-200 text-violet-800 hover:border-violet-500 hover:bg-violet-50 dark:border-violet-900/60 dark:text-violet-300 dark:hover:bg-violet-900/20',
    chipActive: 'border-violet-500 bg-violet-100 text-violet-900 dark:border-violet-400 dark:bg-violet-900/40 dark:text-violet-100',
    tag: 'bg-violet-100 text-violet-800 hover:bg-violet-200 dark:bg-violet-900/40 dark:text-violet-200 dark:hover:bg-violet-900/60',
  },
  pink: {
    chip: 'border-pink-200 text-pink-800 hover:border-pink-500 hover:bg-pink-50 dark:border-pink-900/60 dark:text-pink-300 dark:hover:bg-pink-900/20',
    chipActive: 'border-pink-500 bg-pink-100 text-pink-900 dark:border-pink-400 dark:bg-pink-900/40 dark:text-pink-100',
    tag: 'bg-pink-100 text-pink-800 hover:bg-pink-200 dark:bg-pink-900/40 dark:text-pink-200 dark:hover:bg-pink-900/60',
  },
  orange: {
    chip: 'border-orange-200 text-orange-800 hover:border-orange-500 hover:bg-orange-50 dark:border-orange-900/60 dark:text-orange-300 dark:hover:bg-orange-900/20',
    chipActive: 'border-orange-500 bg-orange-100 text-orange-900 dark:border-orange-400 dark:bg-orange-900/40 dark:text-orange-100',
    tag: 'bg-orange-100 text-orange-800 hover:bg-orange-200 dark:bg-orange-900/40 dark:text-orange-200 dark:hover:bg-orange-900/60',
  },
  fuchsia: {
    chip: 'border-fuchsia-200 text-fuchsia-800 hover:border-fuchsia-500 hover:bg-fuchsia-50 dark:border-fuchsia-900/60 dark:text-fuchsia-300 dark:hover:bg-fuchsia-900/20',
    chipActive: 'border-fuchsia-500 bg-fuchsia-100 text-fuchsia-900 dark:border-fuchsia-400 dark:bg-fuchsia-900/40 dark:text-fuchsia-100',
    tag: 'bg-fuchsia-100 text-fuchsia-800 hover:bg-fuchsia-200 dark:bg-fuchsia-900/40 dark:text-fuchsia-200 dark:hover:bg-fuchsia-900/60',
  },
  slate: {
    chip: 'border-slate-200 text-slate-700 hover:border-slate-500 hover:bg-slate-50 dark:border-slate-800 dark:text-slate-400 dark:hover:bg-slate-800/40',
    chipActive: 'border-slate-500 bg-slate-100 text-slate-900 dark:border-slate-400 dark:bg-slate-800 dark:text-slate-100',
    tag: 'bg-slate-100 text-slate-700 hover:bg-slate-200 dark:bg-slate-800 dark:text-slate-300 dark:hover:bg-slate-700',
  },
};
