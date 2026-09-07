import * as React from 'react';
import { SocialLinks, defaultSocialLinks } from 'shaden-shaar-site';

/** The default row: email, Google Scholar, GitHub, LinkedIn, X. */
export const Default = () => <SocialLinks />;

/** Larger icons, as used beneath the hero bio and in the contact block. */
export const Large = () => <SocialLinks iconSize={20} />;

/** Smaller icons, as used in the site footer. */
export const FooterSize = () => <SocialLinks iconSize={17} />;

/** A reduced set, for contexts where only scholarly profiles belong. */
export const ScholarlyOnly = () => {
  const all = defaultSocialLinks(20);
  return <SocialLinks links={all.filter((l) => l.label !== 'X' && l.label !== 'LinkedIn')} />;
};
