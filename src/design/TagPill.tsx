import * as React from 'react';

export type TagColor =
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

/** Tag colour → Tailwind classes. Mirrors COLOR_CLASSES in src/data/projects.ts. */
const TAG_CLASSES: Record<TagColor, string> = {
  amber: 'bg-amber-100 text-amber-800 hover:bg-amber-200 dark:bg-amber-900/40 dark:text-amber-200 dark:hover:bg-amber-900/60',
  sky: 'bg-sky-100 text-sky-800 hover:bg-sky-200 dark:bg-sky-900/40 dark:text-sky-200 dark:hover:bg-sky-900/60',
  emerald: 'bg-emerald-100 text-emerald-800 hover:bg-emerald-200 dark:bg-emerald-900/40 dark:text-emerald-200 dark:hover:bg-emerald-900/60',
  rose: 'bg-rose-100 text-rose-800 hover:bg-rose-200 dark:bg-rose-900/40 dark:text-rose-200 dark:hover:bg-rose-900/60',
  teal: 'bg-teal-100 text-teal-800 hover:bg-teal-200 dark:bg-teal-900/40 dark:text-teal-200 dark:hover:bg-teal-900/60',
  violet: 'bg-violet-100 text-violet-800 hover:bg-violet-200 dark:bg-violet-900/40 dark:text-violet-200 dark:hover:bg-violet-900/60',
  pink: 'bg-pink-100 text-pink-800 hover:bg-pink-200 dark:bg-pink-900/40 dark:text-pink-200 dark:hover:bg-pink-900/60',
  orange: 'bg-orange-100 text-orange-800 hover:bg-orange-200 dark:bg-orange-900/40 dark:text-orange-200 dark:hover:bg-orange-900/60',
  fuchsia: 'bg-fuchsia-100 text-fuchsia-800 hover:bg-fuchsia-200 dark:bg-fuchsia-900/40 dark:text-fuchsia-200 dark:hover:bg-fuchsia-900/60',
  slate: 'bg-slate-100 text-slate-700 hover:bg-slate-200 dark:bg-slate-800 dark:text-slate-300 dark:hover:bg-slate-700',
};

export interface TagPillProps {
  /** Short label, e.g. "Fact-checking". */
  label: string;
  /** Colour family identifying the research thread. */
  color?: TagColor;
  /** Renders as a link when set; otherwise a static span. */
  href?: string;
  /** Renders as a button when set; takes precedence over href. */
  onClick?: () => void;
  /** Filter-chip pressed state, styled via aria-pressed. */
  pressed?: boolean;
  className?: string;
}

/**
 * Small rounded pill marking which research thread a paper belongs to.
 * Appears under publication cards and as the filter control on the
 * publications page. One colour per research project.
 */
export function TagPill({
  label,
  color = 'slate',
  href,
  onClick,
  pressed,
  className = '',
}: TagPillProps) {
  // The pressed state needs its own affordance: aria-pressed alone is
  // invisible, so an active filter would look identical to an inactive one.
  const pressedClasses = pressed ? ' ring-1 ring-inset ring-current font-semibold' : '';
  const classes = `rounded-full px-2 py-0.5 text-[11px] font-medium transition-colors ${TAG_CLASSES[color]}${pressedClasses} ${className}`;

  if (onClick) {
    return (
      <button type="button" onClick={onClick} aria-pressed={pressed} className={classes}>
        {label}
      </button>
    );
  }
  if (href) {
    return (
      <a href={href} className={classes}>
        {label}
      </a>
    );
  }
  return <span className={classes}>{label}</span>;
}

export default TagPill;
