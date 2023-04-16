<!-- routes/signup/+page.svelte -->
<script lang="ts">
	import { enhance } from "$app/forms";
</script>

<div>
	<h1>Create an account</h1>
	<form method="POST" use:enhance>
		<label for="name">name</label><br />
		<input id="name" name="name" /><br />

		<label for="username">username</label><br />
		<input id="username" name="username" /><br />

		<label for="email">email</label><br />
		<input id="email" name="email" /><br />
		<label for="password">Password</label><br />
		<input type="password" id="password" name="password" /><br />
		<input type="submit" value="Signup" class="btn btn-primary"/>
	</form>
</div>