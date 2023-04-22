import type { Actions, PageServerLoad } from "./$types";
import { error, fail, redirect } from "@sveltejs/kit";
import { prisma } from "$lib/server/prisma";

export const load: PageServerLoad = async ({ params }) => {
    const getPost = async () => {
        const post = await prisma.post.findUnique({
            where: {
                id: BigInt(params.postId)
            },
        })
        if (!post) {
            throw error(404, "post not found")
        }
        return post
    }

    return {
        post: getPost()
    }
};

export const actions: Actions = {
    default: async ({ request, params }) => {
        const { title, excerpt, content } = Object.fromEntries(await request.formData()) as { title: string, excerpt: string, content: string}

        try {
            await prisma.post.update({
                where: {
                    id: BigInt(params.postId)
                },
                data: {
                    title,
                    excerpt,
                    content
                },
            })
        } catch (error) {
            console.log(error)
            return fail(500, { message: "something went wrong" })
        }

        throw redirect(302, '/')
    }
};