// See https://kit.svelte.dev/docs/types#app

import type { PrismaClient } from "@prisma/client";

// for information about these interfaces
declare global {
	namespace App {
		interface Locals {
			auth: import("lucia-auth").AuthRequest;
		}
		// interface Error {}
		// interface Locals {}
		// interface PageData {}
		// interface Platform {}
	}
	// eslint-disable-next-line no-var
	var prisma: PrismaClient
}

/// <reference types="lucia-auth" />
declare global {
	namespace Lucia {
		type Auth = import("$lib/lucia").Auth;
		// eslint-disable-next-line @typescript-eslint/ban-types
		type UserAttributes = {
			name: string;
			username: string;
			email: string;
		};
	}
}

export {};
