import * as React from 'react';
import { SocialLinks } from './SocialLinks';

export interface FooterProps {
  /** Display name shown on the first line. */
  name?: string;
  /** Affiliation line rendered beneath the name, before the copyright year. */
  affiliation?: string;
  /** Copyright year. Defaults to the current year. */
  year?: number;
  className?: string;
}

/**
 * Site footer: name and affiliation on the left, profile icons on the right,
 * separated from the page by a hairline rule. Stacks vertically on narrow
 * viewports.
 */
export function Footer({
  name = 'Shaden Shaar',
  affiliation = 'PhD candidate, Cornell CS',
  year = new Date().getFullYear(),
  className = '',
}: FooterProps) {
  return (
    <footer className={`mt-24 border-t border-zinc-200 dark:border-zinc-800 ${className}`}>
      <div className="mx-auto flex max-w-6xl flex-col items-start justify-between gap-4 px-5 py-10 text-sm text-ink-muted dark:text-zinc-400 sm:flex-row sm:items-center sm:px-8">
        <div>
          <p className="text-ink dark:text-zinc-200">{name}</p>
          <p className="mt-0.5 text-xs text-ink-subtle dark:text-zinc-500">
            {affiliation} · © {year}
          </p>
        </div>
        <SocialLinks iconSize={17} />
      </div>
    </footer>
  );
}

export default Footer;
