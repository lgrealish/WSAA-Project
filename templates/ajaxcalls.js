$(document).ready(function () {
  loadPlayers();

  function loadPlayers() {
      $.ajax({
          url: '/players',
          method: 'GET',
          success: function (players) {
              $('#playerTable tbody').empty();
              players.forEach(function (player) {
                  $('#playerTable tbody').append(`
                      <tr id="${player.id}">
                          <td>${player.name}</td>
                          <td>${player.club}</td>
                          <td>${player.age}</td>
                          <td>${player.position}</td>
                          <td>
                              <button class="btn btn-info" onclick="editPlayer('${player.name}')">Edit</button>
                              <button class="btn btn-danger" onclick="deletePlayer('${player.name}')">Delete</button>
                          </td>
                      </tr>
                  `);
              });
          },
          error: function (err) {
              console.error('Error fetching players:', err);
          }
      });
  }

  window.savePlayer = function () {
      const id = $('#playerId').val();
      const playerData = {
          Name: $('#name').val(),
          Club: $('#club').val(),
          Age: $('#age').val(),
          Position: $('#position').val()
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
              },
              error: function (err) {
                  console.error('Error updating player:', err);
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
              },
              error: function (err) {
                  console.error('Error creating player:', err);
              }
          });
      }
  };

  window.deletePlayer = function (name) {
      if (confirm('Are you sure you want to delete this player?')) {
          $.ajax({
              url: `/players/${name}`,
              method: 'DELETE',
              success: function () {
                  loadPlayers();
              },
              error: function (err) {
                  console.error('Error deleting player:', err);
              }
          });
      }
  };
});
