module.exports = function open (link) {
  $$.html(`
    <div style="position: relative; padding-bottom: 550px; padding-top: 25px; height: 0;">
      <iframe src="${link}" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div><br>
    <a href="${link}" style="margin: 10px 0">Open in StatSim</a>
  `)
}
