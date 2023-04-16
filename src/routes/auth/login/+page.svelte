<script lang="ts">
	import { enhance } from "$app/forms";
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
			</div>
			<div>
				<label class="label" for="password">
					<span class="text-base label-text">Password</span>
				</label>
				<input type="password" name="password" placeholder="Enter Password" class="w-full input input-bordered input-primary" />
			</div>
			<div>
				<a href="/" class="float-right mr-2 text-xs text-rpimary-content hover:underline hover:text-blue-600">Forget Password?</a>
			</div>
			<div>
				<button type="submit" class="btn btn-primary">Login</button>
			</div>
		</form>
	</div>
</div>