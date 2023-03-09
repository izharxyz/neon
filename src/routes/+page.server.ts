import { fail } from "@sveltejs/kit";
import { prisma } from "$lib/server/prisma";
import type { Actions, PageServerLoad } from "./$types";

export const load: PageServerLoad = async () => {
    return {
        posts: await prisma.post.findMany()
    }
};

export const actions: Actions = {
    createPost: async ({ request }) => {
        const { title, content } = Object.fromEntries(await request.formData()) as { 
            title: string, 
            content: string
        }

        try {
            await prisma.post.create({
                data: {
                    title,
                    content
                }
            })
        } catch (err) {
            console.log(err)
            return fail(500, { message: 'fff'})
        }

        return {
            status: 201
        }
    },

    deletePost: async ({ url }) => {
        const id = url.searchParams.get('id')
        if (!id) {
            return fail(400, {message: 'invalid request'})
        }

        try {
            await prisma.post.delete({
                where: {
                    id: BigInt(id)
                }
            })
        } catch (error) {
            console.log(error)
            return fail(500, {message: 'something went wrong'})
        }

        return {
            status: 200
        }
    }
};