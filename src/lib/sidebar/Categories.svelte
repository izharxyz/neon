<script lang="ts">
    export let profile = "/images/profile.jpg";
</script>

<div class="card w-full border border-primary-content">
    <div class="card-body">
        <h2 class="card-title text-primary border-b border-primary-content pb-5">Categories</h2>
        
        <div class="card w-full mt-5 bg-base-100 shadow-xl border border-primary-content p-3">
            <div class="flex flex-row items-center">
                <img src={profile} alt="profile-pic" class="w-10 h-10 rounded-full"/>
                <h3 class="ml-5">Web dev</h3>
            </div>
        </div>
        <div class="card w-full mt-5 bg-base-100 shadow-xl border border-primary-content p-3">
            <div class="flex flex-row items-center">
                <img src={profile} alt="profile-pic" class="w-10 h-10 rounded-full"/>
                <h3 class="ml-5">Mobile dev</h3>
            </div>
        </div>
        <div class="card w-full mt-5 bg-base-100 shadow-xl border border-primary-content p-3">
            <div class="flex flex-row items-center">
                <img src={profile} alt="profile-pic" class="w-10 h-10 rounded-full"/>
                <h3 class="ml-5">Linux</h3>
            </div>
        </div>
        <div class="card w-full mt-5 bg-base-100 shadow-xl border border-primary-content p-3">
            <div class="flex flex-row items-center">
                <img src={profile} alt="profile-pic" class="w-10 h-10 rounded-full"/>
                <h3 class="ml-5">Blockchain</h3>
            </div>
        </div>
    </div>
</div>