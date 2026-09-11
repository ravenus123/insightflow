"""Initial InsightFlow schema."""
from alembic import op
import sqlalchemy as sa
revision="0001_initial"
down_revision=None
branch_labels=None
depends_on=None

def upgrade():
    op.create_table("users",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("email",sa.String(320),nullable=False),sa.Column("name",sa.String(120),nullable=False),sa.Column("password_hash",sa.Text(),nullable=False),sa.Column("created_at",sa.DateTime(),nullable=False),sa.UniqueConstraint("email"))
    op.create_index("ix_users_email","users",["email"],unique=True)
    op.create_table("projects",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("owner_id",sa.Integer(),sa.ForeignKey("users.id"),nullable=True),sa.Column("name",sa.String(160),nullable=False),sa.Column("description",sa.Text(),nullable=False),sa.Column("currency",sa.String(8),nullable=False),sa.Column("created_at",sa.DateTime(),nullable=False),sa.Column("updated_at",sa.DateTime(),nullable=False))
    op.create_table("datasets",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("public_id",sa.String(64),nullable=False),sa.Column("project_id",sa.Integer(),sa.ForeignKey("projects.id"),nullable=True),sa.Column("filename",sa.String(255),nullable=False),sa.Column("storage_path",sa.Text(),nullable=False),sa.Column("row_count",sa.Integer(),nullable=False),sa.Column("column_count",sa.Integer(),nullable=False),sa.Column("mapping_json",sa.JSON(),nullable=True),sa.Column("created_at",sa.DateTime(),nullable=False))
    op.create_index("ix_datasets_public_id","datasets",["public_id"],unique=True)
    op.create_table("reports",sa.Column("id",sa.Integer(),primary_key=True),sa.Column("project_id",sa.Integer(),sa.ForeignKey("projects.id"),nullable=True),sa.Column("title",sa.String(180),nullable=False),sa.Column("report_type",sa.String(20),nullable=False),sa.Column("summary_json",sa.JSON(),nullable=False),sa.Column("created_at",sa.DateTime(),nullable=False))

def downgrade():
    op.drop_table("reports");op.drop_index("ix_datasets_public_id",table_name="datasets");op.drop_table("datasets");op.drop_table("projects");op.drop_index("ix_users_email",table_name="users");op.drop_table("users")
