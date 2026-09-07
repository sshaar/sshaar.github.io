import * as React from 'react';
import { TagPill, type TagColor } from './TagPill';

export interface PublicationTag {
  label: string;
  color?: TagColor;
  href?: string;
}

export interface PublicationCardProps {
  /** Paper title. Rendered in the display serif. */
  title: string;
  /** Full author list, in order. */
  authors: string[];
  /** Venue as displayed, e.g. "CVPR" or "TACL". */
  venue: string;
  /** Publication year. */
  year: number;
  /** Author name to bold within the author list — the site owner. */
  me?: string;
  /** Links the title to the paper when set. */
  url?: string;
  /** Figure or teaser image URL. Falls back to a venue placeholder tile. */
  image?: string;
  /** One-to-three sentence summary shown under the authors. */
  description?: string;
  /** Award or honour, rendered as a trophy badge above the title. */
  award?: string;
  /** Marks a Findings-track paper in the metadata line. */
  findings?: boolean;
  /** Research-thread tags shown beneath the entry. */
  tags?: PublicationTag[];
  className?: string;
}

const TrophyIcon = () => (
  <svg
    width="13"
    height="13"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth={2}
    strokeLinecap="round"
    strokeLinejoin="round"
    aria-hidden="true"
  >
    <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6" />
    <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18" />
    <path d="M4 22h16" />
    <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22" />
    <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22" />
    <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z" />
  </svg>
);

/**
 * Featured paper entry for the home page's "Selected publications" section.
 * Lays a figure (or a venue placeholder tile) beside the paper's metadata,
 * title, author list with the site owner bolded, summary, and thread tags.
 * An optional award badge sits above the title.
 */
export function PublicationCard({
  title,
  authors,
  venue,
  year,
  me,
  url,
  image,
  description,
  award,
  findings,
  tags = [],
  className = '',
}: PublicationCardProps) {
  return (
    <article className={`grid items-start gap-4 sm:grid-cols-[11rem_1fr] sm:gap-6 ${className}`}>
      <div className="max-w-[16rem] sm:max-w-none">
        {image ? (
          <img
            src={image}
            alt={`Figure from ${title}`}
            loading="lazy"
            className="aspect-[4/3] w-full rounded-lg bg-zinc-100 object-cover ring-1 ring-zinc-200 dark:bg-zinc-900 dark:ring-zinc-800"
          />
        ) : (
          <div
            className="flex aspect-[4/3] w-full items-center justify-center rounded-lg bg-zinc-100/60 px-3 text-center ring-1 ring-zinc-200 dark:bg-zinc-900/60 dark:ring-zinc-800"
            aria-hidden="true"
          >
            <span className="font-mono text-[11px] uppercase tracking-widest text-ink-subtle dark:text-zinc-500">
              {venue} {year}
            </span>
          </div>
        )}
      </div>

      <div className="min-w-0">
        <p className="meta mb-1.5">
          {venue} {year}
          {findings ? ' · Findings' : ''}
        </p>

        {award && (
          <p className="mb-1.5 flex items-center gap-1.5 text-xs font-medium text-amber-700 dark:text-amber-400">
            <TrophyIcon />
            {award}
          </p>
        )}

        {url ? (
          <a
            href={url}
            className="font-serif text-lg leading-snug text-ink transition-colors hover:text-accent-700 dark:text-zinc-100 dark:hover:text-accent-300 md:text-xl"
          >
            {title}
          </a>
        ) : (
          <span className="font-serif text-lg leading-snug text-ink dark:text-zinc-100 md:text-xl">
            {title}
          </span>
        )}

        <p className="mt-1.5 text-sm text-ink-muted dark:text-zinc-400">
          {authors.map((a, i) => {
            const sep = i < authors.length - 1 ? ', ' : '';
            return a === me ? (
              <React.Fragment key={a}>
                <span className="font-semibold text-ink dark:text-zinc-200">{a}</span>
                {sep}
              </React.Fragment>
            ) : (
              <React.Fragment key={`${a}-${i}`}>
                {a}
                {sep}
              </React.Fragment>
            );
          })}
        </p>

        {description && (
          <p className="mt-2 max-w-prose text-sm leading-relaxed text-ink-muted dark:text-zinc-400">
            {description}
          </p>
        )}

        {tags.length > 0 && (
          <div className="mt-2.5 flex flex-wrap gap-1.5">
            {tags.map((t) => (
              <TagPill key={t.label} label={t.label} color={t.color} href={t.href} />
            ))}
          </div>
        )}
      </div>
    </article>
  );
}

export default PublicationCard;
