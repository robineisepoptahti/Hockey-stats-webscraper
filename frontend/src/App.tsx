import "./App.css";
import PlayersTable from "./components/playersTable";
import InputForm from "./components/inputForm";
import PlayersToolbar from "./components/playersToolbar";
import { useState, useEffect } from "react";
import playerService from "./services/players";
import type { Player } from "./types";

function App() {
  // State to hold player data
  const [players, setPlayers] = useState<Player[]>([]);

  //Fetch when needed
  useEffect(() => {
    const fetchPlayers = async () => {
      //Fetching data from backend
      const fetchedPlayers: Player[] = await playerService.getAll();
      setPlayers(fetchedPlayers);
      //Caching
      try {
        localStorage.setItem("playersList", JSON.stringify(fetchedPlayers));
      } catch (e) {
        console.error("Could not save data:", e);
      }
    };
    fetchPlayers();
  }, []);
  return (
    <>
      <div id="bar">
        <PlayersToolbar />
      </div>
      <h1>Hockey statistics</h1>
      <div id="input">
        <InputForm setPlayers={setPlayers} />
      </div>
      <div>
        <PlayersTable players={players} setPlayers={setPlayers} />
      </div>
    </>
  );
}

export default App;
