<script lang="ts">
	import { enhance } from "$app/forms";
</script>

<div class="relative flex flex-col justify-center h-[600px] overflow-hidden">
	<div class="w-full p-6 m-auto card bg-base-100 border border-primary-content lg:max-w-lg">
		<h1 class="text-3xl font-semibold text-center text-primary">Register</h1>
		<form method="POST" class="space-y-4" use:enhance>
			<div>
				<label class="label" for="name">
					<span class="text-base label-text">Name</span>
				</label>
				<input name="name" type="text" placeholder="Your name" class="w-full input input-bordered input-primary" />
			</div>
			<div>
				<label class="label" for="username">
					<span class="text-base label-text">Username</span>
				</label>
				<input name="username" type="text" placeholder="A unique username" class="w-full input input-bordered input-primary" />
			</div>
			<div>
				<label class="label" for="email">
					<span class="text-base label-text">Email</span>
				</label>
				<input name="email" type="text" placeholder="Email Address" class="w-full input input-bordered input-primary" />
			</div>
			<div>
				<label class="label" for="password">
					<span class="text-base label-text">Password</span>
				</label>
				<input type="password" name="password" placeholder="Enter Password" class="w-full input input-bordered input-primary" />
			</div>
			<div>
				<button type="submit" class="btn btn-primary">Join Now !</button>
			</div>
		</form>
	</div>
</div>