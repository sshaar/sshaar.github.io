import * as React from 'react';
import { SectionHeading } from 'shaden-shaar-site';

/** The common case — a bare serif heading opening a section. */
export const Plain = () => <SectionHeading>Experience</SectionHeading>;

/** With a mono eyebrow label above it, as used on the publications page. */
export const WithLabel = () => <SectionHeading label="Publications">Publications</SectionHeading>;

/** With a baseline-aligned action link on the right. */
export const WithAction = () => (
  <SectionHeading
    action={
      <a href="/publications/" className="link text-sm text-ink-muted dark:text-zinc-400">
        All 47 publications →
      </a>
    }
  >
    Selected publications
  </SectionHeading>
);

/** As a page title. */
export const AsPageTitle = () => (
  <SectionHeading as="h1" label="PhD Candidate · Cornell University">
    Contact
  </SectionHeading>
);
