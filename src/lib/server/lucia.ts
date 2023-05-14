import lucia from 'lucia-auth';
import { sveltekit } from 'lucia-auth/middleware';
import prismaAdapter from '@lucia-auth/adapter-prisma';
import { prisma } from '$lib/server/prisma';
import { dev } from '$app/environment';

export const auth = lucia({
	adapter: prismaAdapter(prisma),
	env: dev ? 'DEV' : 'PROD',
	middleware: sveltekit(),
	transformDatabaseUser: (userData) => {
		return {
			userId: userData.id,
			name: userData.name,
			username: userData.username,
			email: userData.email
		};
	}
});

export type Auth = typeof auth;
