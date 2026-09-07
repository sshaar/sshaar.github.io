import * as React from 'react';

export interface SectionHeadingProps {
  /** Heading text, set in the display serif. */
  children: React.ReactNode;
  /** Optional mono uppercase eyebrow rendered above the heading. */
  label?: string;
  /** Optional right-aligned action, typically a "see all" link. */
  action?: React.ReactNode;
  /** Heading level to render. Defaults to h2. */
  as?: 'h1' | 'h2' | 'h3';
  className?: string;
}

/**
 * Section heading used to open each block of the home page — Experience,
 * Publications, Education, Contact. Pairs an optional mono eyebrow label with
 * a serif heading, and can carry a right-aligned action link on the baseline.
 */
export function SectionHeading({
  children,
  label,
  action,
  as: Tag = 'h2',
  className = '',
}: SectionHeadingProps) {
  const heading = <Tag className="section-heading">{children}</Tag>;

  if (!action) {
    return (
      <div className={className}>
        {label && <p className="section-label mb-3">{label}</p>}
        {heading}
      </div>
    );
  }

  return (
    <div className={className}>
      {label && <p className="section-label mb-3">{label}</p>}
      <div className="flex flex-wrap items-baseline justify-between gap-x-6 gap-y-1">
        {heading}
        {action}
      </div>
    </div>
  );
}

export default SectionHeading;
