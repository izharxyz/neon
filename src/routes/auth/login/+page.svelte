<script lang="ts">
	import { enhance } from "$app/forms";
	export let form;
</script>

<div class="relative flex flex-col justify-center h-[600px] overflow-hidden">
	<div class="w-full p-6 m-auto card bg-base-100 border border-primary-content lg:max-w-lg">
		<h1 class="text-3xl font-semibold text-center text-primary">Login</h1>
		<form method="POST" class="space-y-4" use:enhance>
			<div>
				<label class="label" for="email">
					<span class="text-base label-text">Email</span>
				</label>
				<input name="email" type="text" placeholder="Email Address" class="w-full input input-bordered input-primary" />
				<label class="label" for="email">
					{#if form?.errors?.email}
						<span class="text-xs label-text text-error">{form?.errors?.email[0]}</span>
					{/if}
				</label>
			</div>
			<div>
				<label class="label" for="password">
					<span class="text-base label-text">Password</span>
				</label>
				<input type="password" name="password" placeholder="Enter Password" class="w-full input input-bordered input-primary" />
				<label class="label" for="password">
					{#if form?.errors?.password}
						<span class="text-xs label-text text-error">{form?.errors?.password[0]}</span>
					{/if}
				</label>
			</div>
			<div>
				<a href="/auth/register" class="float-right mr-2 hover:underline">Need an account? <span class="text-secondary">Register</span></a>
			</div>
			<div>
				<button type="submit" class="btn btn-primary mt-4">Login</button>
			</div>
		</form>
	</div>
</div>