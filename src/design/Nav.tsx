import * as React from 'react';

export interface NavLink {
  href: string;
  label: string;
  /** Opens in a new tab and is never marked active. */
  external?: boolean;
}

export interface NavProps {
  /** Wordmark shown at the left. */
  brand?: string;
  /** Navigation entries, in order. */
  links?: NavLink[];
  /** Current path, used to mark the active link. */
  currentPath?: string;
  /** Renders the theme toggle button. */
  showThemeToggle?: boolean;
  className?: string;
}

export const defaultNavLinks: NavLink[] = [
  { href: '/', label: 'Home' },
  { href: '/publications/', label: 'Publications' },
  { href: '/cv.pdf', label: 'CV', external: true },
];

const SunMoonIcon = () => (
  <svg
    width="18"
    height="18"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth={2}
    strokeLinecap="round"
    strokeLinejoin="round"
    aria-hidden="true"
  >
    <path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z" />
  </svg>
);

/**
 * Sticky site header: serif wordmark at the left, primary navigation and the
 * theme toggle at the right. The bar is translucent with a backdrop blur so
 * content scrolls beneath it. Below the sm breakpoint the links collapse
 * behind a menu button.
 */
export function Nav({
  brand = 'Shaden Shaar',
  links = defaultNavLinks,
  currentPath = '/',
  showThemeToggle = true,
  className = '',
}: NavProps) {
  const isActive = (link: NavLink) =>
    !link.external &&
    (currentPath === link.href || (link.href !== '/' && currentPath.startsWith(link.href)));

  return (
    <header
      className={`sticky top-0 z-30 border-b border-zinc-200/80 bg-paper/85 backdrop-blur-md dark:border-zinc-800/80 dark:bg-zinc-950/85 ${className}`}
    >
      <div className="mx-auto flex max-w-6xl items-center justify-between gap-3 px-5 py-3.5 sm:px-8">
        <a href="/" className="shrink-0 font-serif text-lg tracking-tight text-ink dark:text-zinc-100">
          {brand}
        </a>

        <nav className="hidden items-center gap-6 sm:flex" aria-label="Site">
          {links.map((link) => (
            <a
              key={link.href}
              href={link.href}
              className={`nav-link${isActive(link) ? ' is-active' : ''}`}
              aria-current={isActive(link) ? 'page' : undefined}
              target={link.external ? '_blank' : undefined}
              rel={link.external ? 'noopener noreferrer' : undefined}
            >
              {link.label}
            </a>
          ))}
          {showThemeToggle && (
            <button
              type="button"
              aria-label="Toggle theme"
              className="rounded-md p-2 text-ink-muted transition-colors hover:text-ink dark:text-zinc-400 dark:hover:text-zinc-100"
            >
              <SunMoonIcon />
            </button>
          )}
        </nav>

        <div className="flex items-center gap-1 sm:hidden">
          {showThemeToggle && (
            <button
              type="button"
              aria-label="Toggle theme"
              className="rounded-md p-2 text-ink-muted transition-colors hover:text-ink dark:text-zinc-400 dark:hover:text-zinc-100"
            >
              <SunMoonIcon />
            </button>
          )}
          <button
            type="button"
            aria-label="Toggle menu"
            className="rounded-md p-2 text-ink-muted transition-colors hover:text-ink dark:text-zinc-400 dark:hover:text-zinc-100"
          >
            <svg
              width="20"
              height="20"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth={2}
              strokeLinecap="round"
              aria-hidden="true"
            >
              <line x1="4" y1="7" x2="20" y2="7" />
              <line x1="4" y1="12" x2="20" y2="12" />
              <line x1="4" y1="17" x2="20" y2="17" />
            </svg>
          </button>
        </div>
      </div>
    </header>
  );
}

export default Nav;
