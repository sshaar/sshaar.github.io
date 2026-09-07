import * as React from 'react';
import { TagPill } from 'shaden-shaar-site';

/** Every research thread on the site, each in its assigned colour. */
export const ResearchThreads = () => (
  <div className="flex flex-wrap gap-1.5">
    <TagPill label="Long-form Generation" color="sky" />
    <TagPill label="Fact-checking" color="emerald" />
    <TagPill label="Propaganda" color="rose" />
    <TagPill label="COVID-19" color="teal" />
    <TagPill label="Argument" color="violet" />
    <TagPill label="Clinical NLP" color="amber" />
  </div>
);

/** Filter-chip form used on the publications page, showing both states. */
export const AsFilterChips = () => (
  <div className="flex flex-wrap gap-1.5">
    <TagPill label="Fact-checking" color="emerald" onClick={() => {}} pressed />
    <TagPill label="Propaganda" color="rose" onClick={() => {}} />
    <TagPill label="COVID-19" color="teal" onClick={() => {}} />
  </div>
);

/** Linked form, as it appears beneath a publication card. */
export const AsLink = () => (
  <TagPill label="Long-form Generation" color="sky" href="/publications/" />
);
