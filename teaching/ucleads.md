---
layout: page
title: UC LEADS
---
<section>
	<header class="major">
		<h2>Introduction to Research</h2>
	</header>
			<p><span class="image right"><img src="../assets/images/ucleads_logo.png" alt="" /></span>Part of my work at UC Davis is working with extraordinary undergraduate students in the UC-wide program, UC LEADS. During the summer I co-teach a course on research, and teach students some of the often overlooked skills in research.</p>
			<h3>Lessons</h3>
	<ul class="alt">
	{% for lesson_pp in site.ucleads2020 %}
			<li><a href=" {{ lesson_pp.url }} " class="icon fa-book"><span class="label"></span></a> <a href=" {{ lesson_pp.url }} ">{{ lesson_pp.title }}</a></li>
	{% endfor %}	
</ul>
</section>
<hr class="major" />