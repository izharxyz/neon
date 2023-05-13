import { fail, redirect } from "@sveltejs/kit";
import { auth } from "$lib/server/lucia";
import { z } from 'zod'
import type { PageServerLoad, Actions } from "./$types";

// If the user exists, redirect authenticated users to the profile page.
export const load: PageServerLoad = async ({ locals }) => {
	const session = await locals.auth.validate();
	if (session) throw redirect(302, "/");
};

// zod object to validate user input 
const registerSchema = z.object({
	email: z.string({required_error: 'Email is required'}).min(6, {message: 'Invalid Email'}).max(32, {message: 'Invalid Email'}).email(),
	password: z.string({required_error: 'This field is required'}).min(8, {message: 'Password must contain 8 characters minimum'}).max(64, {message: 'Password must contain 64 characters maximum'}).trim(),
})

export const actions: Actions = {
	default: async ({ request, locals }) => {
		const formData = Object.fromEntries(await request.formData())
	
		try {
			const form = registerSchema.parse(formData)

			console.log("Form Validation SUCCESSFULL!!")
			console.log(form)

			try {
				const key = await auth.useKey("email", form.email, form.password);
				const session = await auth.createSession(key.userId);
				locals.auth.setSession(session);
			} catch {
				// invalid credentials
				return fail(400);
			}
		// eslint-disable-next-line @typescript-eslint/no-explicit-any
		} catch(err: any) {
			const { fieldErrors: errors } = err.flatten()
			// eslint-disable-next-line @typescript-eslint/no-unused-vars
			const { password, ...rest } = formData

			console.log(errors)
			return {
				data: rest,
				errors
			}
		}
	}
};