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
    return [...byYear.entries()].sort((a, b) => b[0] - a[0]);
  }, [filtered]);

  return (
    <div>
      <div className="mb-6 space-y-4">
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
              className="ml-1 text-xs text-ink-muted hover:text-ink dark:text-zinc-300 dark:hover:text-zinc-200 underline underline-offset-2"
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
          className="w-full rounded-md border border-zinc-200 dark:border-zinc-700 bg-transparent px-3 py-2 text-sm focus:border-accent-600 focus:outline-none focus:ring-1 focus:ring-accent-600"
        />
        <div className="text-xs text-ink-muted dark:text-zinc-300">
          {filtered.length} of {publications.length} publications
          {active.size > 0 ? ` · filtered by ${active.size} project${active.size > 1 ? 's' : ''}` : ''}
        </div>
      </div>

      {grouped.length === 0 && (
        <p className="text-sm text-ink-muted dark:text-zinc-300 py-8">No publications match these filters.</p>
      )}

      {grouped.map(([year, pubs]) => (
        <section key={year} className="mb-10">
          <h3
            id={`pub-${year}`}
            className="toc-item text-sm font-mono text-ink-muted dark:text-zinc-400 mb-2 tracking-wider scroll-mt-24"
          >
            {year}
          </h3>
          <ul>
            {pubs.map((pub) => (
              <li key={pub.id} className="pub-card">
                <div className="flex flex-col gap-1.5">
                  <div>
                    {pub.url ? (
                      <a href={pub.url} className="font-medium text-ink dark:text-zinc-200 hover:text-accent-700 dark:hover:text-accent-300 transition-colors">
                        {pub.title}
                      </a>
                    ) : (
                      <span className="font-medium text-ink dark:text-zinc-200">{pub.title}</span>
                    )}
                  </div>
                  <div className="text-sm text-ink-muted dark:text-zinc-300">
                    {formatAuthors(pub.authors, me)}
                  </div>
                  <div className="flex flex-wrap items-center gap-x-3 gap-y-1 text-xs text-ink-muted dark:text-zinc-400">
                    <span className="italic">{pub.venueShort ?? pub.venue}</span>
                    {pub.findings && (
                      <>
                        <span>·</span>
                        <span>Findings</span>
                      </>
                    )}
                    <span>·</span>
                    <span>{typeLabel[pub.type]}</span>
                    {pub.citations !== undefined && pub.citations > 0 && (
                      <>
                        <span>·</span>
                        <span>{pub.citations} citation{pub.citations === 1 ? '' : 's'}</span>
                      </>
                    )}
                  </div>
                  {pub.projects.length > 0 && (
                    <div className="mt-1 flex flex-wrap gap-1.5">
                      {pub.projects.map((slug) => {
                        const proj = projects.find((p) => p.slug === slug);
                        if (!proj) return null;
                        const colors = COLOR_CLASSES[proj.color];
                        return (
                          <button
                            key={slug}
                            type="button"
                            onClick={() => toggle(slug)}
                            className={`text-[11px] rounded-full px-2 py-0.5 font-medium transition-colors ${colors.tag}`}
                          >
                            {proj.short ?? proj.name}
                          </button>
                        );
                      })}
                    </div>
                  )}
                </div>
              </li>
            ))}
          </ul>
        </section>
      ))}
    </div>
  );
}
