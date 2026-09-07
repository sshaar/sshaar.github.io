import * as React from 'react';
import { Footer } from 'shaden-shaar-site';

/** The site footer as shipped. */
export const Default = () => <Footer year={2026} />;

/** With a different affiliation line. */
export const CustomAffiliation = () => (
  <Footer name="Shaden Shaar" affiliation="Research Scientist" year={2027} />
);
