$(document).ready(function () {
  loadPlayers();

  function loadPlayers() {
      $.ajax({
          url: '/api/players',
          method: 'GET',
          success: function (players) {
              $('#playerTable tbody').empty();
              players.forEach(function (player) {
                  $('#playerTable tbody').append(`
                      <tr data-id="${player.id}">
                          <td>${player.name}</td>
                          <td>${player.club}</td>
                          <td>${player.age}</td>
                          <td>${player.position}</td>
                          <td>
                              <button class="btn btn-info" onclick="editPlayer(${player.id})">Edit</button>
                              <button class="btn btn-danger" onclick="deletePlayer(${player.id})">Delete</button>
                          </td>
                      </tr>
                  `);
              });
          }
      });
  }

  window.showCreatePlayerForm = function () {
      $('#playerId').val('');
      $('#name').val('');
      $('#club').val('');
      $('#age').val('');
      $('#position').val('');
      $('#modalTitle').text('Add Player');
      $('#playerModal').modal('show');
  };

  window.savePlayer = function () {
      const id = $('#playerId').val();
      const playerData = {
          name: $('#name').val(),
          club: $('#club').val(),
          age: $('#age').val(),
          position: $('#position').val()
      };

      if (id) {
          // Update existing player
          $.ajax({
              url: `/players/${id}`,
              method: 'PUT',
              contentType: 'application/json',
              data: JSON.stringify(playerData),
              success: function () {
                  $('#playerModal').modal('hide');
                  loadPlayers();
              }
          });
      } else {
          // Create new player
          $.ajax({
              url: '/players',
              method: 'POST',
              contentType: 'application/json',
              data: JSON.stringify(playerData),
              success: function () {
                  $('#playerModal').modal('hide');
                  loadPlayers();
              }
          });
      }
  };

  window.editPlayer = function (id) {
      // Fetch player data to populate the form for editing
      $.ajax({
          url: `/players/${id}`,
          method: 'GET',
          success: function (player) {
              $('#playerId').val(player.id);
              $('#name').val(player.name);
              $('#club').val(player.club);
              $('#age').val(player.age);
              $('#position').val(player.position);
              $('#modalTitle').text('Edit Player');
              $('#playerModal').modal('show');
          }
      });
  };

  window.deletePlayer = function (id) {
      // Delete player by ID
      if (confirm('Are you sure you want to delete this player?')) {
          $.ajax({
              url: `/players/${id}`,
              method: 'DELETE',
              success: function () {
                  loadPlayers();
              }
          });
      }
  };
});
