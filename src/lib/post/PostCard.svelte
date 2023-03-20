<script lang="ts">
    export let title = "An Amazing Post";
    export let thumbnail = "/images/borg.jpg";
    export let excerpt = "An amazing post which is a must read!";
    // export let time: number = 5;
</script>

<div class="card card-side bg-base-100 mt-6">
    <figure class="rounded-2xl"><img src={thumbnail} alt="Post" class="w-64 h-64"/></figure>
    <div class="card-body">
      <h2 class="card-title">{title}</h2>
      <p>{excerpt}</p>
      <div class="card-actions justify-end">
      </div>
    </div>
</div>