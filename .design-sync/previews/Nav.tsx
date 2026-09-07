import * as React from 'react';
import { Nav } from 'shaden-shaar-site';

/** The header as it appears on the home page. */
export const HomeActive = () => <Nav currentPath="/" />;

/** On a subpage, the matching link is marked active. */
export const PublicationsActive = () => <Nav currentPath="/publications/" />;

/** Without the theme toggle, for embeds that manage theme themselves. */
export const WithoutThemeToggle = () => <Nav currentPath="/blog/" showThemeToggle={false} />;
