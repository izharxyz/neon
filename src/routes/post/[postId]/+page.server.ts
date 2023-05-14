import { prisma } from '$lib/server/prisma';
import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params }) => {
	const getPost = async () => {
		const post = await prisma.post.findUnique({
			where: {
				id: BigInt(params.postId)
			}
		});
		if (!post) {
			throw error(404, 'post not found');
		}
		return post;
	};

	return {
		post: getPost()
	};
};
