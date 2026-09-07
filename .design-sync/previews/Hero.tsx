import * as React from 'react';
import { Hero } from 'shaden-shaar-site';

// Inline portrait stand-in: the real /portrait.jpg lives in the site's public
// dir, which the design bundle doesn't ship, so a data URI keeps the image
// slot honest without a broken reference.
const PORTRAIT =
  'data:image/svg+xml;utf8,' +
  encodeURIComponent(
    `<svg xmlns="http://www.w3.org/2000/svg" width="280" height="373" viewBox="0 0 280 373">
      <rect width="280" height="373" fill="#e7e5e4"/>
      <circle cx="140" cy="140" r="58" fill="#c8c4c0"/>
      <path d="M40 373c0-58 45-96 100-96s100 38 100 96z" fill="#c8c4c0"/>
    </svg>`,
  );

const bio = (
  <>
    <p>
      Hello! I am a final-year CS PhD student at <a href="https://www.cornell.edu" className="link">Cornell
      University</a>, fortunate to be advised by Prof. <a href="https://www.cs.cornell.edu/home/cardie/" className="link">Claire
      Cardie</a>. I am currently most excited about working out what models actually need from long
      inputs: what they have to locate in a document or a two-hour film, and when locating the right
      piece isn&rsquo;t enough.
    </p>
    <p>
      Before this, I did my undergraduate at Carnegie Mellon University, and then spent two years as
      a research assistant at the <a href="https://www.hbku.edu.qa/en/qcri" className="link">Qatar
      Computing Research Institute</a>, working on automated fact-checking, propaganda detection and
      COVID-19 misinformation.
    </p>
  </>
);

/** The home page hero: label, name, two-paragraph bio, portrait, profile icons. */
export const WithPortrait = () => <Hero portrait={PORTRAIT}>{bio}</Hero>;

/** Text-only, for pages that lead with the bio rather than the face. */
export const TextOnly = () => <Hero>{bio}</Hero>;

/** Without the profile icon row. */
export const WithoutSocialLinks = () => (
  <Hero portrait={PORTRAIT} showSocialLinks={false}>
    {bio}
  </Hero>
);
