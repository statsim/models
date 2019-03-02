module.exports = function iframer (link) {
  $$.html(`
    <div class="iframer-wrapper" style="position: relative; padding-bottom: 550px; padding-top: 25px; height: 0;">
      <iframe src="${link}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div><br>
    <a class="iframer-link" href="${link}" target="_blank" style="margin: 10px 0;">Open in ${link.split('/')[2]}</a>
  `)
}
