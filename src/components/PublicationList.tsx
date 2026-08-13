import { useMemo, useState } from 'react';
import type { Publication } from '../data/publications';
import type { ResearchProject } from '../data/projects';
import { COLOR_CLASSES } from '../data/projects';

interface Props {
  publications: Publication[];
  projects: ResearchProject[];
  me: string;
}

const typeLabel: Record<Publication['type'], string> = {
  journal: 'Journal',
  conference: 'Conference',
  workshop: 'Workshop',
  preprint: 'Preprint',
};

// Approximate calendar month each venue is typically held (1 = Jan … 12 = Dec).
// Used to order venues within a year chronologically. Journals and unknown
// venues fall back to 12 so they sort last.
const VENUE_MONTH: Record<string, number> = {
  ECIR: 4,
  LREC: 5,
  JHLT: 5,
  ICWSM: 6,
  NAACL: 6,
  CVPR: 6,
  ACL: 7,
  NLP4IF: 7,
  SemEval: 7,
  IJCAI: 8,
  ArgMining: 8,
  CLEF: 9,
  CEUR: 9,
  RANLP: 9,
  LCN: 10,
  EMNLP: 11,
  COLING: 12,
  ICMLA: 12,
  TACL: 12,
  FACT: 12,
};

const venueMonth = (v: string): number => VENUE_MONTH[v] ?? 12;

function formatAuthors(authors: string[], me: string) {
  return authors.map((a, i) => {
    const isMe = a === me;
    return (
      <span key={i}>
        <span className={isMe ? 'font-semibold text-ink dark:text-zinc-200' : ''}>{a}</span>
        {i < authors.length - 1 ? ', ' : ''}
      </span>
    );
  });
}

export default function PublicationList({ publications, projects, me }: Props) {
  const [active, setActive] = useState<Set<string>>(new Set());
  const [query, setQuery] = useState('');

  const toggle = (slug: string) => {
    setActive((prev) => {
      const next = new Set(prev);
      if (next.has(slug)) next.delete(slug);
      else next.add(slug);
      return next;
    });
  };

  const clear = () => setActive(new Set());

  const filtered = useMemo(() => {
    const q = query.trim().toLowerCase();
    return publications.filter((pub) => {
      if (active.size > 0 && !pub.projects.some((p) => active.has(p))) return false;
      if (q) {
        const hay = `${pub.title} ${pub.authors.join(' ')} ${pub.venue}`.toLowerCase();
        if (!hay.includes(q)) return false;
      }
      return true;
    });
  }, [publications, active, query]);

  const grouped = useMemo(() => {
    const byYear = new Map<number, Publication[]>();
    for (const pub of filtered) {
      const list = byYear.get(pub.year) ?? [];
      list.push(pub);
      byYear.set(pub.year, list);
    }
    // Within each year, order papers by the venue's typical calendar month so
    // the year reads chronologically.
    return [...byYear.entries()]
      .sort((a, b) => b[0] - a[0])
      .map(([year, pubs]) => ({
        year,
        pubs: [...pubs].sort(
          (a, b) =>
            venueMonth(a.venueShort ?? a.venue) - venueMonth(b.venueShort ?? b.venue) ||
            (a.venueShort ?? a.venue).localeCompare(b.venueShort ?? b.venue),
        ),
      }));
  }, [filtered]);

  return (
    <div>
      <div className="mb-8 space-y-4">
        <div className="flex flex-wrap items-center gap-2">
          {projects.map((proj) => {
            const isActive = active.has(proj.slug);
            const colors = COLOR_CLASSES[proj.color];
            return (
              <button
                key={proj.slug}
                type="button"
                className={`inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-medium transition-colors ${
                  isActive ? colors.chipActive : colors.chip
                }`}
                aria-pressed={isActive}
                onClick={() => toggle(proj.slug)}
              >
                {proj.short ?? proj.name}
              </button>
            );
          })}
          {active.size > 0 && (
            <button
              type="button"
              onClick={clear}
              className="ml-1 text-xs text-ink-muted underline underline-offset-2 hover:text-ink dark:text-zinc-400 dark:hover:text-zinc-200"
            >
              clear
            </button>
          )}
        </div>
        <input
          type="search"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search title, author, venue…"
          className="w-full rounded-lg border border-zinc-200 bg-transparent px-3.5 py-2 text-sm focus:border-accent-600 focus:outline-none focus:ring-1 focus:ring-accent-600 dark:border-zinc-700"
        />
        <p className="meta">
          {filtered.length} of {publications.length} publications
          {active.size > 0 ? ` · filtered by ${active.size} project${active.size > 1 ? 's' : ''}` : ''}
        </p>
      </div>

      {grouped.length === 0 && (
        <p className="py-8 text-sm text-ink-muted dark:text-zinc-400">
          No publications match these filters.
        </p>
      )}

      {grouped.map(({ year, pubs }) => (
        <section key={year} className="mb-4">
          <div className="grid gap-x-8 sm:grid-cols-[4rem_1fr]">
            <h2
              id={`pub-${year}`}
              className="scroll-mt-24 pt-5 font-serif text-2xl text-ink-subtle dark:text-zinc-600 sm:sticky sm:top-20 sm:self-start"
            >
              {year}
            </h2>
            <ul className="min-w-0 divide-y divide-zinc-200 dark:divide-zinc-800">
              {pubs.map((pub) => (
                <li key={pub.id} className="py-5">
                  <p className="meta mb-1">
                    <span className="italic">{pub.venueShort ?? pub.venue}</span>
                    {pub.findings ? ' · Findings' : ''} · {typeLabel[pub.type]}
                  </p>
                  {pub.award && (
                    <p className="mb-1 flex items-center gap-1.5 text-xs font-medium text-amber-700 dark:text-amber-400">
                      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
                        <path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"></path>
                        <path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"></path>
                        <path d="M4 22h16"></path>
                        <path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"></path>
                        <path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"></path>
                        <path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"></path>
                      </svg>
                      {pub.award}
                    </p>
                  )}
                  {pub.url ? (
                    <a
                      href={pub.url}
                      className="font-medium leading-snug text-ink transition-colors hover:text-accent-700 dark:text-zinc-200 dark:hover:text-accent-300"
                    >
                      {pub.title}
                    </a>
                  ) : (
                    <span className="font-medium leading-snug text-ink dark:text-zinc-200">{pub.title}</span>
                  )}
                  <p className="mt-1 text-sm text-ink-muted dark:text-zinc-400">
                    {formatAuthors(pub.authors, me)}
                  </p>
                  {pub.projects.length > 0 && (
                    <div className="mt-2 flex flex-wrap gap-1.5">
                      {pub.projects.map((slug) => {
                        const proj = projects.find((p) => p.slug === slug);
                        if (!proj) return null;
                        const colors = COLOR_CLASSES[proj.color];
                        return (
                          <button
                            key={slug}
                            type="button"
                            onClick={() => toggle(slug)}
                            className={`rounded-full px-2 py-0.5 text-[11px] font-medium transition-colors ${colors.tag}`}
                          >
                            {proj.short ?? proj.name}
                          </button>
                        );
                      })}
                    </div>
                  )}
                </li>
              ))}
            </ul>
          </div>
        </section>
      ))}
    </div>
  );
}
