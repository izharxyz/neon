import { fail, redirect } from "@sveltejs/kit";
import { auth } from "$lib/server/lucia";
import { z } from "zod";
import type { PageServerLoad, Actions } from "./$types";

export const load: PageServerLoad = async ({ locals }) => {
	const session = await locals.auth.validate();
	if (session) throw redirect(302, "/");
	return {};
};

// zod object to validate user input 
const registerSchema = z.object({
	name: z.string({required_error: 'Name is required'}).min(1, {message: 'Name is required'}).max(64, {message: 'Name must be less than 64 characters'}).trim(),
	username: z.string({required_error: 'Username is required'}).min(1, {message: 'Username is required'}).max(64, {message: 'Username must be less than 64 characters'}).trim(),
	email: z.string({required_error: 'Email is required'}).min(6, {message: 'Invalid Email'}).max(32, {message: 'Invalid Email'}).email(),
	password: z.string({required_error: 'This field is required'}).min(8, {message: 'Password must contain 8 characters minimum'}).max(64, {message: 'Password must contain 64 characters maximum'}).trim(),
	passwordConfirm: z.string({required_error: 'This field is required'}).min(8, {message: 'Password must contain 8 characters minimum'}).max(64, {message: 'Password must contain 64 characters maximum'}).trim()
})


export const actions: Actions = {
	default: async ({ request, locals }) => {
		const formData = Object.fromEntries(await request.formData())
	
		try {
			const form = registerSchema.parse(formData)

			console.log("Form Validation SUCCESSFULL!!")
			console.log(form)

			// pass validated form data to lucia and try for register
			try {
				const user = await auth.createUser({
					primaryKey: {
						providerId: "email",
						providerUserId: form.email,
						password: form.password
					},
					attributes: {
						name: form.name,
						username: form.username,
						email: form.email
					}
				});
				
				console.log("user created SUCCESSFULLY")
				console.log({user})
	
				const session = await auth.createSession(user.userId);

				// creates session after successfull register; no need to login
				locals.auth.setSession(session);

			} catch(e) {
				console.log({e})
				// username already in use
				return fail(400);
			}

		// eslint-disable-next-line @typescript-eslint/no-explicit-any
		} catch(err: any) {
			const { fieldErrors: errors } = err.flatten()
			// eslint-disable-next-line @typescript-eslint/no-unused-vars
			const { password, passwordConfirm, ...rest } = formData

			console.log(errors)
			return {
				data: rest,
				errors
			}
		}
	}
};