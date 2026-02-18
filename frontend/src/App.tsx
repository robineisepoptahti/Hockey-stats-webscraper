import "./App.css";
import PlayersTable from "./components/playersTable";
import InputForm from "./components/inputForm";
import Toolbar from "./components/toolbar";
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
      <div>
        <Toolbar />
      </div>
      <h1>Hokcey statistics</h1>
      <div>
        <InputForm setPlayers={setPlayers} />
      </div>
      <div>
        <PlayersTable players={players} />
      </div>
    </>
  );
}

export default App;
