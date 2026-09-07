import * as React from 'react';
import { NewsCard } from 'shaden-shaar-site';

const items = [
  {
    date: 'Jun 2026',
    body: (
      <>
        <em>MovieRecapsQA</em>, our open-ended benchmark for question-answering over full-length
        movies, appeared at <strong>CVPR 2026</strong>.
      </>
    ),
  },
  {
    date: 'May 2026',
    body: (
      <>
        Our <strong>JHLT</strong> paper with NewYork-Presbyterian uses an LLM for thematic analysis
        of accepted heart-transplant exception requests.
      </>
    ),
  },
  {
    date: 'Aug 2025',
    body: (
      <>
        Wrapped up a summer as an Applied Scientist Intern at <strong>Zillow</strong>, building
        conversational real-estate agents with reinforcement learning.
      </>
    ),
  },
  {
    date: 'May 2025',
    body: (
      <>
        “Are Triggers Needed for Document-Level Event Extraction?” was published in{' '}
        <strong>TACL</strong>.
      </>
    ),
  },
];

/** The home page feed: four entries, newest marked with an accent dot. */
export const HomePageFeed = () => <NewsCard items={items} />;

/** Without the latest-entry marker, for pages where nothing is "new". */
export const Unmarked = () => <NewsCard items={items.slice(0, 3)} markLatest={false} />;

/** A single entry — the minimum the card renders. */
export const SingleEntry = () => <NewsCard items={items.slice(0, 1)} />;
