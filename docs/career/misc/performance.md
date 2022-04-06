# Performance

How can we think critically about performance and how to make a website faster?

### Keys to Performance
There are three places where work needs to happen when displaying websites:
1. GET request to server
2. Server does some work, sends data back
3. Display data from server

So we can improve the client side, we can improve our transfer time, and we can improve backend processing. 

Part one of performance we'll focus on critical render path

### Minimize Images
You want to pick the right types of images (jpg, png, gif, svg) and compress them as small as you can without taking from their quality.
- If you want transparency: use a PNG
- If you want animations: use a GIF
- If you want colorful images: use a JPG
- If you want simple icons, logos, illustrations, use SVGs
- Reduce PNG with [TinyPNG](https://tinypng.com/) 
- Reduce JPG with [jpeg-optimizer](http://jpeg-optimizer.com/)
- Try to choose simple illustrations over highly detailed photographs
- Always lower JPG image quality (30-60%)
- Resize image based on size it will be displayed
- Display different sized images for different backgrounds
- Use CDNs like [imgix](https://www.imgix.com/?utm_term=imgix&utm_campaign=adwords-branded&utm_source=adwords&utm_medium=ppc&hsa_tgt=kwd-347244981599&hsa_grp=98890898611&hsa_src=g&hsa_net=adwords&hsa_mt=p&hsa_ver=3&hsa_ad=456649958299&hsa_acc=8534109361&hsa_kw=imgix&hsa_cam=9210499657&gclid=Cj0KCQiA0MD_BRCTARIsADXoopbaiwxfrkrZx62gTorkL9bRTwyBzhM8GmSj43MR-8P0QpWrNtiBiB8aAlP3EALw_wcB)
- Remove image metadata

### [HTTP/2](https://developers.google.com/web/fundamentals/performance/http2/)
Update to HTTP that updates network latency

### Resources
- [Performance analysis in a table](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/reference#activities)
- [Analyze frames per second (FPS)](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/reference#fps)
- [Monitor: CPU usage, JS heap size, DOM nodes (event listeners, documents, frames per page), layouts and style recalculations per second](https://developers.google.com/web/updates/2017/11/devtools-release-notes#perf-monitor)
- [View Interactions](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/reference#interactions)
- [Find scroll performance issues in realtime](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/reference#scrolling-performance-issues)
- [View painting events in real time](https://developers.google.com/web/tools/chrome-devtools/evaluate-performance/reference#paint-flashing)

For additional resources see Ch. 53 in course content



 (../index.md)