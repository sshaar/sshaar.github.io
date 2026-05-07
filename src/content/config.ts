import { defineCollection, z } from 'astro:content';

const research = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    short: z.string().optional(),
    summary: z.string(),
    status: z.enum(['active', 'past']).default('active'),
    order: z.number().default(100),
    pubs: z.array(z.string()).default([]), // publication ids to associate
  }),
});

const blog = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    date: z.coerce.date(),
    draft: z.boolean().default(false),
    tags: z.array(z.string()).default([]),
  }),
});

const teaching = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    role: z.string(),
    institution: z.string().default('Cornell University'),
    term: z.string(),
    year: z.number(),
    url: z.string().url().optional(),
    order: z.number().default(100),
  }),
});

const experiences = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    organization: z.string(),
    location: z.string().optional(),
    startDate: z.coerce.date(),
    endDate: z.coerce.date().optional(),
    ongoing: z.boolean().default(false),
    url: z.string().url().optional(),
    description: z.string().optional(),
    bullets: z.array(z.string()).default([]),
  }),
});

export const collections = { research, blog, teaching, experiences };
