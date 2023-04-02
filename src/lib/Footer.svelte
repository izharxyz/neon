<script>
    import Icon from '@iconify/svelte';
</script>

<div class="card grid grid-cols-1 md:grid-cols-3 p-5 md:p-20 border border-primary-content gap-12">
   <div class="col-span-1">
        <div>
            <a href="/" class="logo">
                ZEDCODES
            </a> 
        </div>
        <p class="mt-3">
            When an unknown prnoto sans took a galley and scrambled it to make specimen
            book not only five When an unknown prnoto sans took a galley and scrambled it to five centurie.
        </p>
        <h3 class="font-bold mt-5 text-xl">Contact</h3>
        <p>myop.asfuck@email.org</p>
   </div>
   <div class="col-span-1">
        <h1 class="font-bold text-xl">Categories</h1>
        <h3 class="mt-5">Web dev</h3>
        <h3 class="mt-2">Mobile dev</h3>
        <h3 class="mt-2">Linux</h3>
   </div>
   <div class="col-span-1">
        <h1 class="font-bold text-xl">Newsletter</h1>
        <p class="mt-5">Sign up to be first to receive the latest stories inspiring us, case studies, and industry news.</p>
        <form action="" class="mt-5">
            <label for="">
                Enter your email address
            </label> 
            <div class="mt-5 relative">
                <input type="text" placeholder="username@site.com" class="input input-bordered w-full pr-16" /> 
                <button class="btn bg-gradient-to-r from-primary to-secondary absolute top-0 right-0 rounded-l-none">Subscribe</button>
            </div>
        </form>
   </div>
   <div class="col-span-1 md:col-span-3 border-t border-primary-content flex flex-row justify-between pt-5 md:pt-20 md:mt-5">
        <p>View source on <span class="text-primary hover:text-primary-focus transition duration-150 cursor-pointer">Github</span></p>
        <div class="flex flex-row">
            <a href="https://github.com/zzedddd">
                <Icon icon='mdi:github'class="icon"/>
            </a>
            <Icon icon='mdi:linkedin'class="icon"/>
            <Icon icon='ant-design:twitter-circle-filled'class="icon"/>
        </div>
   </div>
</div>