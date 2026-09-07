import * as React from 'react';
import { SocialLinks } from './SocialLinks';

export interface HeroProps {
  /** Display name, set in the display serif. */
  name?: string;
  /** Mono uppercase eyebrow above the name. */
  label?: string;
  /** Biography paragraphs. Pass JSX to keep inline links. */
  children: React.ReactNode;
  /** Portrait image URL. Omit to render text only. */
  portrait?: string;
  /** Alt text for the portrait. Defaults to the name. */
  portraitAlt?: string;
  /** Renders the profile icon row beneath the bio. */
  showSocialLinks?: boolean;
  className?: string;
}

/**
 * Opening block of the home page: eyebrow label, name, biography, and a
 * portrait. The portrait sits to the right on wider viewports and moves above
 * the text when the layout stacks, so the face is the first thing seen on a
 * phone. Profile icons close the block.
 */
export function Hero({
  name = 'Shaden Shaar',
  label = 'PhD Candidate · Cornell University',
  children,
  portrait,
  portraitAlt,
  showSocialLinks = true,
  className = '',
}: HeroProps) {
  return (
    <section className={className}>
      {label && <p className="section-label mb-3">{label}</p>}
      <h1 className="font-serif text-4xl leading-tight text-ink dark:text-zinc-100 md:text-5xl">
        {name}
      </h1>

      <div className="mt-8 grid items-start gap-8 sm:grid-cols-[minmax(0,1fr)_auto] sm:gap-10">
        <div className="order-2 min-w-0 sm:order-1">
          <div className="space-y-4 leading-relaxed text-ink-muted dark:text-zinc-300">{children}</div>
          {showSocialLinks && <SocialLinks className="mt-7" iconSize={20} />}
        </div>

        {portrait && (
          <img
            src={portrait}
            alt={portraitAlt ?? name}
            width={280}
            height={326}
            className="order-1 aspect-[3/4] w-44 shrink-0 rounded-xl object-cover ring-1 ring-zinc-200 dark:ring-zinc-800 sm:order-2 sm:w-56 md:w-64"
          />
        )}
      </div>
    </section>
  );
}

export default Hero;
