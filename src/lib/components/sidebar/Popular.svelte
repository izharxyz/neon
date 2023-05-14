<script lang="ts">
	export let title = 'An Amazing Post';
	export let thumbnail = '/images/borg.jpg';
</script>

<div class="card w-full border border-primary-content mt-6">
	<div class="card-body">
		<h2 class="card-title text-primary border-b border-primary-content pb-5">Popular posts</h2>
		<div class="flex flex-row items-center w-full mt-5">
			<img src={thumbnail} alt="profile-pic" class="w-14 h-14 rounded-full" />
			<h3 class="text-base ml-5">{title}</h3>
		</div>
		<div class="flex flex-row items-center w-full mt-5">
			<img src={thumbnail} alt="profile-pic" class="w-14 h-14 rounded-full" />
			<h3 class="text-base ml-5">{title}</h3>
		</div>
		<div class="flex flex-row items-center w-full mt-5">
			<img src={thumbnail} alt="profile-pic" class="w-14 h-14 rounded-full" />
			<h3 class="text-base ml-5">{title}</h3>
		</div>
		<div class="flex flex-row items-center w-full mt-5">
			<img src={thumbnail} alt="profile-pic" class="w-14 h-14 rounded-full" />
			<h3 class="text-base ml-5">{title}</h3>
		</div>
		<div class="flex flex-row items-center w-full mt-5">
			<img src={thumbnail} alt="profile-pic" class="w-14 h-14 rounded-full" />
			<h3 class="text-base ml-5">{title}</h3>
		</div>
	</div>
</div>
