export type Player = {
  id: number | null;
  name: string;
  season_points: number;
  goals: number;
  assists: number;
  games: number;
  team: string;
  team_id: string;
  pId: string;
  sp: number;
  toi: string;
  league: string;
  pm: number;
};

export type PlayersTableProps = {
  players: Player[];
  setPlayers: React.Dispatch<React.SetStateAction<Player[]>>;
};

export type InputFormProps = {
  setPlayers: React.Dispatch<React.SetStateAction<Player[]>>;
};

export type TableMeta = {
  setPlayers: React.Dispatch<React.SetStateAction<Player[]>>;
};

export type RemoveResponse = {
  players: Player[];
  status: number;
};
