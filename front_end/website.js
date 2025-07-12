fetch("http://127.0.0.1:5000/api/tenders")
  .then((res) => res.json())
  .then((data) => {
    const container = document.getElementById("card_container");
    data.forEach((tender) => {
      const card = document.createElement("div");
      card.className = "card";
      card.innerHTML = `
      <div class="card_layer_1">
        <div class="card_orgnisation">${tender.organisation}</div>
        <div class="card_location">${tender.address?.split(",")[0] || ""}</div>
      </div>
      <div class="card_layer_1">
        <div class="card_id">${tender.tender_id}</div>
        <div class="day_left"></div>
      </div>
      <div class="card_title">${tender.item_description}</div>
    `;
      container.appendChild(card);
    });
  });
