/**
 * Design system for sshaar.github.io.
 *
 * These are the real React components the site renders (Astro mounts them via
 * @astrojs/react). They are styled with the site's own Tailwind config and the
 * component classes in src/styles/global.css — there is no separate token set.
 */
export { Nav, defaultNavLinks, type NavProps, type NavLink } from './Nav';
export { Hero, type HeroProps } from './Hero';
export { NewsCard, type NewsCardProps, type NewsItem } from './NewsCard';
export {
  PublicationCard,
  type PublicationCardProps,
  type PublicationTag,
} from './PublicationCard';
export { SectionHeading, type SectionHeadingProps } from './SectionHeading';
export { TagPill, type TagPillProps, type TagColor } from './TagPill';
export { Footer, type FooterProps } from './Footer';
export {
  SocialLinks,
  defaultSocialLinks,
  type SocialLinksProps,
  type SocialLink,
} from './SocialLinks';
