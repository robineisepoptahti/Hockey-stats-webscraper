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
      const players: Player[] = await playerService.getAll();
      setPlayers(players);
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
        <PlayersTable players={players} />
      </div>
    </>
  );
}

export default App;
