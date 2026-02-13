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
};

export type InputFormProps = {
  setPlayers: React.Dispatch<React.SetStateAction<Player[]>>;
};
