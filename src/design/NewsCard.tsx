import * as React from 'react';

export interface NewsItem {
  /** Short date label, e.g. "Jun 2026". */
  date: string;
  /** The item body. Plain text or inline markup. */
  body: React.ReactNode;
}

export interface NewsCardProps {
  /** Entries, newest first. */
  items: NewsItem[];
  /** Marks the newest entry with an accent dot. */
  markLatest?: boolean;
  className?: string;
}

/**
 * Dated activity feed for the home page — papers accepted, internships
 * finished, talks given. Renders as a raised card with a hairline divider
 * between entries and a mono date gutter that collapses above the text on
 * narrow viewports. The newest entry can carry an accent dot.
 */
export function NewsCard({ items, markLatest = true, className = '' }: NewsCardProps) {
  return (
    <ul className={`card divide-y divide-zinc-200 dark:divide-zinc-800 ${className}`}>
      {items.map((n, i) => (
        <li
          key={`${n.date}-${i}`}
          className="flex flex-col gap-1 px-5 py-4 sm:flex-row sm:items-baseline sm:gap-6 sm:px-6"
        >
          <span className="meta flex shrink-0 items-center gap-1.5 sm:w-24">
            {markLatest && i === 0 && (
              <span
                className="h-1.5 w-1.5 rounded-full bg-accent-600 dark:bg-accent-400"
                aria-hidden="true"
              />
            )}
            {n.date}
          </span>
          <p className="text-[15px] leading-relaxed text-ink-muted dark:text-zinc-300">{n.body}</p>
        </li>
      ))}
    </ul>
  );
}

export default NewsCard;
